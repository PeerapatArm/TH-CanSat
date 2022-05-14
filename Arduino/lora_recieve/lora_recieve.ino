#include <SPI.h>
// Example By ArduinoAll
#define LoRa Serial2// Serial board ทีม Hemit
void setup() {
  Serial.begin(9600);
  LoRa.begin(9600);
  Serial.println("LoRa Receiver");
}
void loop() {
  if (LoRa.available()) {
    Serial.write(LoRa.read());
    
  }
}
