import time 
from playsound import playsound
print(time.strftime("%H:%M"))
alarm_time=input("Enter the time to set alarm:(HH:MM): ")
while time.strftime("%H:%M") !=alarm_time:
    time.sleep(1)
print("Time to wake up!!!")
playsound("D:/alarm.mp3")