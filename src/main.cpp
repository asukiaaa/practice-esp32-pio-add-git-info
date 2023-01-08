#include <Arduino.h>

#ifndef STR_INFO_GIT
#define STR_INFO_GIT "no-info"
#endif

void setup() {
  Serial.begin(115200);
  Serial.println("start");
}

void loop() {
  Serial.print("STR_INFO_GIT: ");
  Serial.println(STR_INFO_GIT);
  Serial.println(millis());
  delay(1000);
}
