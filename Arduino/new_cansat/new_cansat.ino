#include <Wire.h>
#include <SPI.h>
#include <SD.h>
#include <Adafruit_Sensor.h>
#include <Adafruit_BME280.h>
#include <Adafruit_FXAS21002C.h>
#include <Adafruit_FXOS8700.h>
#include <TinyGPSPlus.h>

#define gpsserial Serial2 //GPS
#define LoRa Serial3  // cansat
#define SEALEVELPRESSURE_HPA 1013.25

TinyGPSPlus gps;
Adafruit_BME280 bme280;
Adafruit_FXAS21002C gyro = Adafruit_FXAS21002C(0x0021002C);
Adafruit_FXOS8700 accel = Adafruit_FXOS8700(0x8700A, 0x8700B);

int state = 0;

uint32_t time0 = 0;
uint32_t time1 = 0;
uint32_t PKG = 0;
uint32_t lastExecuted = 0;
uint32_t lastChecked = 0;

String dataString = "";
String dataString2 = "";

float GYRX, GYRY, GYRZ, ACCX, ACCY, ACCZ;
float TEM = 0;
float ALT = 0;
float LAT = 0;
float LNG = 0;

char file[50];

File datafile;

void get_gps() {
  while (gpsserial.available()) {
    char c = gpsserial.read();
    gps.encode(c);
  }
  LAT = (float) gps.location.lat();
  LNG = (float) gps.location.lng();
}

void get_bme() {
  TEM = bme280.readTemperature();
  ALT = bme280.readAltitude(SEALEVELPRESSURE_HPA);
}

void get_gyro() {
  sensors_event_t event;
  gyro.getEvent(&event);

  GYRX = (float) event.gyro.x;
  GYRY = (float) event.gyro.y;
  GYRZ = (float) event.gyro.z;
}

void get_accel() {
  sensors_event_t aevent, mevent;
  accel.getEvent(&aevent, &mevent);

  ACCX = aevent.acceleration.x;
  ACCY = aevent.acceleration.y;
  ACCZ = aevent.acceleration.z;
}

void setup() {
  Serial.begin(9600);
  LoRa.begin(9600);
  gpsserial.begin(9600);
  Wire.begin();
  SD.begin(10);

  if (!gyro.begin()) Serial.println("gyro init error");

  if (!accel.begin()) Serial.println("accel init error");

  if (!bme280.begin(0x76, &Wire))
    Serial.println("BME280 cannot init");

  Serial.println("finish setting up I2C");

  int idx = 0;
  String C = ("data_" + String(idx) + ".txt");
  C.toCharArray(file, 20);
  while (SD.exists(file)) {
    idx++;
    C = ("data_" + String(idx) + ".txt");
    C.toCharArray(file, 20);
  }
  datafile = SD.open(file, FILE_WRITE);
}

void loop() {
  get_gps();
  time0 = millis();
  if (time0 - lastChecked >= 100) {
    get_bme();
    get_accel();
    get_gyro();
    get_gps();
    lastChecked = time0;
  }

  time0 = millis();
  if (millis() - lastExecuted >= 500) {
    lastExecuted = millis();
    dataString = String(PKG++) + ",";
    dataString += String(ALT, 2) + ",";
    dataString += String(GYRX, 2) + ",";
    dataString += String(GYRY, 2) + ",";
    dataString += String(GYRZ, 2) + ",";
    dataString += String(ACCX, 2) + ",";
    dataString += String(ACCY, 2) + ",";
    dataString += String(ACCZ, 2) + ",";
    dataString += String(TEM, 2) + ",";
    dataString += String(LAT, 6) + ",";
    dataString += String(LNG, 6) + "$";
    //Serial.println(ALT);
    //LoRa.println(ALT);
    
    //Serial.println(TEM);
    LoRa.println(dataString);
    Serial.println(dataString);
    if (datafile) {
      datafile.println(dataString);
      datafile.flush();
    }
  }
}
