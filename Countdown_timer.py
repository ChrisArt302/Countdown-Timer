# Countdown seconds timer with alarm
import time
from playsound import playsound

# ask user for input
def countdown_t():
    t = int(input("How many seconds do you want to countdown to: "))
    print("Timer is running")
    while t:
        mins = t // 60
        secs = t % 60
        timer = '{:02d}:{:02d}'.format(mins, secs)
        print('\r', timer, end='')
        time.sleep(1)
        t -= 1
        if t == 0:
            print('\r 0:00')
countdown_t()
print("Time is up")
playsound('alarm_sound.wav')
