#include <SD.h> //-- include SD card library
#define SD_ChipSelectPin 4
#include <TMRpcm.h> //-- playback of pcm/wav audio
#include <SPI.h>

TMRpcm player;

void setup() {
  player.speakerPin = 10;

  Serial.begin(9600);
  while (!Serial) {
    ; // wait for serial port to connect. Needed for native USB port only
  }

  if(!SD.begin(SD_ChipSelectPin)){
    Serial.println("SD Card failed to open");
    return;
  }else{
    Serial.println("SD Card opened.");
  }

  player.setVolume(7);
  player.play("bullion.wav");

}

void loop() {

}
