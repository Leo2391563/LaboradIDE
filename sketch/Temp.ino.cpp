#include <Arduino.h>
#line 1 "C:\\Users\\user\\Documents\\GitHub\\laborad_ide\\main\\Temp\\Temp.ino"
#line 1 "C:\\Users\\user\\Documents\\GitHub\\laborad_ide\\main\\Temp\\Temp.ino"
void setup();
#line 5 "C:\\Users\\user\\Documents\\GitHub\\laborad_ide\\main\\Temp\\Temp.ino"
void loop();
#line 1 "C:\\Users\\user\\Documents\\GitHub\\laborad_ide\\main\\Temp\\Temp.ino"
void setup() {
  pinMode(13, OUTPUT);
}

void loop() {
  digitalWrite(13,1);
  delay(1000);
  digitalWrite(13,0);
  delay(1000);
}


