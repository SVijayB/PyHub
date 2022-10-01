import datetime
from pygame import mixer

Hour = int(input("At what hour do you want the alarm? ")) 
Min = int(input("Specify exact minutes ")) 
amPm = str(input("AM or PM? ")) 
if (amPm == "pm"): 
    alarmH = alarmH + 12

while(True):
    if(Hour == datetime.datetime.now().hour and Min == datetime.datetime.now().minute): 
    mixer.music.load("your_audio_file.mp3")
    mixer.music.play()
