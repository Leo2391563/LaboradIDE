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




