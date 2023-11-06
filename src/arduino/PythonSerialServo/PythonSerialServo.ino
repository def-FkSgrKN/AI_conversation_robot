#include <Servo.h>

Servo myServo;
int var = 60;

void setup() {
  myServo.attach(9);
  myServo.write(var);
  Serial.begin(9600);
}

void loop() {
  if(Serial.available()>0){
    var = Serial.read();
    myServo.write(var);
    delay(100);
  } 
}
