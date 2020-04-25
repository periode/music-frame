#include <SD.h> //-- include SD card library
#define SD_ChipSelectPin 4
#include <TMRpcm.h> //-- playback of pcm/wav audio
#include <SPI.h>

TMRpcm player;
int track = 1;
int pauseBtn = 5;
int nextBtn = 6;
int prevBtn = 7;

void setup() {
  pinMode(pauseBtn, INPUT_PULLUP);
  pinMode(nextBtn, INPUT_PULLUP);
  pinMode(prevBtn, INPUT_PULLUP);

  player.speakerPin = 9;

  Serial.begin(9600);

  if(!SD.begin(SD_ChipSelectPin)){
    Serial.println("SD Card failed to open");
    return;
  }

  player.setVolume(5);
  player.play("bullion.wav");

}

void loop() {
  while(digitalRead(pauseBtn)==0 || digitalRead(nextBtn)==0 || digitalRead(prevBtn)==0)
  {
    if(digitalRead(pauseBtn)==0)
    {
      player.pause();
      while(digitalRead(pauseBtn)==0);
      delay(200);
    }
    else if(digitalRead(nextBtn)==0)
    {
      if(track<4)//temp should be lesser than no. of songs 
      track=track+1;
      while(digitalRead(nextBtn)==0);
      delay(200);
      song();
    }
    else if(digitalRead(prevBtn)==0)
    {
      if(track>1)
      track=track-1;
      while(digitalRead(prevBtn)==0);
      delay(200);
      song();
    }
  }
}

void song(){
  Serial.println("playing song");
}
