# sound sculpture workshop
===================================

## description
----------------------------

with all the music in the world at the end of our streaming fingertips, it's sometimes hard to think of sounds as something which takes up *space*, something with *weight*, something that can be *built*. and yet, affordable electronics, simple software and cnc machines make it easier than ever to design and construct a musical artefact.

this workshop takes the (very good) excuse of making such a musical artefact to learn the basics of software, hardware, parametric fabrication and sound design, over the course of two days. housed in the zonoteka gallery in neukolln, we will go through all the different steps involved in constructing your own sonified object.

the **electronics** part will include learning the basics of arduino, a hardware prototyping platform, how to connect together a micro-controller, a storage module, an amplifier and an audio exciter. the **software** part will get you introduced to the basics of programming the arduino, in order to program your own playback logic (or, as brian eno would put it, "semi-autonomous generative music"). the **fabrication** component will consist in learning how to design parts on vector software such as illustrator, and how to cut the casing of your object with zonoteka's CNC milling machines, and learning how such a design can arise from programming shapes with parameters, for a unique result. finally, the **sound design** of our object will introduce you to the nitty gritty of audio file formats, and to the craft of writing code to arrange and compose musical sections.

## schedule

----------------------------

pierre - mate - benjamin - andrea

- 10:00
  - welcome, introductions
  - presentation of the day
  - different possibilities
    - product design
    - sound design
    - composition
  
- 10:30
  - writing the code
  - soldering

- 11:30
  - designing the sound
  - recording and editing in audacity

- 12:30
  - break

- 13:30
  - designing the sculpture
  - illustrator/inkscape

- 14:30
  - fabrication
    - foam cutting
    - woodboard assembly
    - painting

## outcomes

- everyone (5 people) was able to finish a build
- no time to paint/coat
- only one cut on the foam machine
- no time to think about / write algorithmic composition
- next time needs a step-up module
- having board to test out soldering was good (also soldering from the reverse side)
- having more examples/several finished versions (both of music and cutouts would be good to give more ideas to the participants)

===================================

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
