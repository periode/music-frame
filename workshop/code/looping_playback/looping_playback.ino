#include <pcmConfig.h>
#include <TMRpcm.h>

#include <SD.h>
#define SD_ChipSelectPin 10    //-- using digital pin 4 on arduino nano 328, can use other pins
#include <SPI.h>

TMRpcm player;

String[] tracks = {"file1.wav", "file2.wav", "file3.wav"};
int totalNumberOfTracks = 3;

void setup(){

  player.speakerPin = 9; //--5,6,11 or 46 on Mega, 9 on Uno, Nano, etc

  Serial.begin(9600);
  
  if (!SD.begin(SD_ChipSelectPin)) {  //-- first things first, check if the card works
    Serial.println("SD fail");  
    return;                           //-- if not, don't do anything more
  }

  Serial.println("SD Success");

  player.setVolume(5);      //-- for obscure reasons, 7 is the maximum value. beyond 7, you get distortion
  player.loop(1);           //-- this enables loop mode
  player.play("bullion.wav"); //-- the sound file "file1.wav" will play each time the arduino powers up, or is reset

}



void loop(){  

  if(!player.isPlaying()){ //-- once we're done playing the track
    
    //-- choose the track to play, randomly
    int trackIndex = (int)(random(0, totalNumberOfTracks));

    player.play(tracks[trackIndex]);


    /*
    //-- pick the following track on the list
    trackIndex++;
    if(trackIndex == totalNumberOfTracks){
      trackIndex = 0;
    }

    player.play(tracks[trackIndex]);

    */
  }
  
}
