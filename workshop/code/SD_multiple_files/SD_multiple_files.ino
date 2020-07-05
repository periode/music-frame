#include <SD.h>                      // need to include the SD library
#define SD_ChipSelectPin 10  //using digital pin 4 on arduino nano 328, can use other pins
#include <SPI.h>

#define NUMBER_OF_SAMPLES 3
String files[NUMBER_OF_SAMPLES] = {"first.wav", "second.wav", "third.wav"};
float durations[NUMBER_OF_SAMPLES] = {8500, 8730, 9290};
int current_file = 0;

float startTime = 0;

void setup() {

  Serial.begin(9600);
  if (!SD.begin(SD_ChipSelectPin)) {  // see if the card is present and can be initialized:
    Serial.println("SD fail");
    return;   // don't do anything more if not
  }

  Serial.println("SD success!");
}

void loop() {
  if(millis() - startTime > durations[current_file]){
    Serial.print("Finished playing ");
    Serial.println(files[current_file]);

    Serial.println("---");

    Serial.print("Picking next file ");
    current_file = (int)(random(0, 3));
    Serial.print(files[current_file]);
    Serial.print(" - ");
    Serial.println(durations[current_file]);
    
    
    startTime = millis();
  }
}
