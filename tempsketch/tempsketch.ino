void setup() {
    // Предустановка. Выполняется один раз
    Serial.begin(9600);
    pinMode(13, OUTPUT);
}

void loop() {
    // Основной цикл программы
    if (Serial.available() > 0) {
    	String nn = Serial.readString();
        if (nn=="1") {
    	    digitalWrite(13,1);
    	    delay(500);
        }
    	Serial.println("aoaoao");
    }
    digitalWrite(13,0);
}


