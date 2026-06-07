import datetime
import time
from playsound import playsound 
 # Make sure the playsound module is installed
# Get alarm time input
alarm_time = input("Enter the alarm time in Hour:Minute:Second AM/PM format: ")
alarm_hour, alarm_minute, alarm_second = map(int, alarm_time[:-3].split(":"))
alarm_period = alarm_time[-2:].upper()
# Ask user for sound file
sound_file = input("Enter the full path of the alarm sound file (e.g., alarm.mp3): ")
print("Setting alarm...")
while True:
    now = datetime.datetime.now()
    current_hour = now.hour
    current_minute = now.minute
    current_second = now.second
    current_period = "AM" if current_hour < 12 else "PM"
    # Convert to 12-hour format
    display_hour = current_hour % 12 or 12
    if (display_hour == alarm_hour and
        current_minute == alarm_minute and
        current_second == alarm_second and
        current_period == alarm_period):
        print("Wake up! It's time!")
        playsound(sound_file)
        break
    time.sleep(1)
