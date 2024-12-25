#include <Arduino.h>
#line 1 "C:\\Users\\user\\Documents\\GitHub\\LaboradIDE\\tempsketch\\tempsketch.ino"
#line 1 "C:\\Users\\user\\Documents\\GitHub\\LaboradIDE\\tempsketch\\tempsketch.ino"
void setup();
#line 7 "C:\\Users\\user\\Documents\\GitHub\\LaboradIDE\\tempsketch\\tempsketch.ino"
void loop();
#line 1 "C:\\Users\\user\\Documents\\GitHub\\LaboradIDE\\tempsketch\\tempsketch.ino"
void setup() {
    // Предустановка. Выполняется один раз
    Serial.begin(9600);
    pinMode(13, OUTPUT);
}

void loop() {
    // Основной цикл программы
    if (Serial.available() > 0) {
        if (Serial.read()=="1") {
    	    digitalWrite(13,1);
        } else {
    	    digitalWrite(13,0);
    	}
    }
}





