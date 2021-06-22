# music

## hardware

the speaker used for now is the [dayton audio daex25fhe-4](https://www.soundimports.eu/en/dayton-audio-daex25fhe-4.html), with:

- 4 Ohm [impedance](http://www.learningaboutelectronics.com/Articles/What-is-speaker-impedance)
- 24 W RMS output

size of the mounted surface: approx 12x8cm, voltage sent: between 5V and 12V

## software

- file constraints
- - uncompressed (PCM / WAV)
- - 8-bit
- - 8-32Khz
- - mono
- SD card storage (16-64Gb)
- library used for playing back files: [TMRpcm](https://github.com/TMRh20/TMRpcm/wiki)

- library for composition: [less concepts](https://maxforlive.com/library/device/6167/less-concepts)

- how to

calculating time of each sample:

```C++
// from https://github.com/TMRh20/TMRpcm/issues/141
void loop(){  

  if(Serial.available()){    
    if(Serial.read() == 'p'){ //send the letter p over the serial monitor to start playback
      uint32_t sampleRate = 0;
      uint32_t fileSize = 0;
      float lengthInSeconds = 0.00;
      myFile = SD.open("calibrat.wav");      
      if(myFile){
        Serial.println("SD is open");
        myFile.seek(24);
        sampleRate = myFile.read();
        sampleRate |= (uint32_t)(myFile.read() << 8);
        sampleRate |= (uint32_t)(myFile.read() << 16);
        sampleRate |= (uint32_t)(myFile.read() << 24);
        fileSize = myFile.size()-44;
        lengthInSeconds = (float)(fileSize) / (float)(sampleRate) ;
        myFile.close();
        
      }else{
        Serial.println("cant open sd");
      }
      Serial.print("Length ");
      Serial.println(lengthInSeconds);
      tmrpcm.play("calibrat.wav");
    }
  }
}
```

## mood

[satoshi ashikawa - still way](https://www.youtube.com/watch?v=f33pvpdXzos) can loop forever
[taku sugimoto](https://www.youtube.com/watch?v=pDUeojq6DrE) - microtonal
