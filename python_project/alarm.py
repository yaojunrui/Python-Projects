from datetime import datetime
from playsound import playsound

alarm_time = input("Please input the alarm time (ex: 09:50:00 am): \n")

alarm_hour = alarm_time[0:2]

alarm_minute = alarm_time[3:5]

alarm_sec = alarm_time[6:8]

alarm_period = alarm_time[9:11].upper()

print("Alarm is set\n")

while True:
    now = datetime.now()
    current_hour = now.strftime("%I")
    current_minute = now.strftime("%M")
    current_seconds = now.strftime("%S")
    current_period = now.strftime("%p")
 
    # 时间判断
    if alarm_period == current_period:
        if alarm_hour == current_hour:
            if alarm_minute == current_minute:
                if alarm_sec == current_seconds:
                    print("起来啦!")
                    # 闹钟铃声
                    playsound('audio.mp3')
                    break