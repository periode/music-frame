#include <Arduino.h>

char *filenames[] = {
  "one",
  "two",
  "three",
  "four"
};

unsigned long timer = 2000.0;
unsigned long start = 0.0;

void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);

  Serial.println("hello");
  Serial.println(filenames[0]);
}

void loop() {
  if(millis() - start > timer){
    start = millis();
    Serial.println(random(0, 10));
  }
}