//Rocket arduino pro mini
#include <Seeed_BME280.h>
#include <Wire.h>
#include <SPI.h>
const int FPV = 7; //pin FPV 7 na krub

BME280 bme280;

void setup() {
  Serial.begin(9600);
  pinMode(FPV,OUTPUT);
  Serial.println("Bme start");
  bme280.init();
}
void get_bme(){
  float pressure = bme280.getPressure();
  Serial.print(String(float(bme280.calcAltitude(pressure)),2));
}
void loop() {
  digitalWrite(FPV,HIGH);
  get_bme();
  delay(2000);

}
