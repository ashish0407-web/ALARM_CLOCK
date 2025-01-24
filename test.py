# Import Required Library
import threading
from tkinter import *


from time import strftime

import datetime

import time

import winsound

from threading import *

# Create Object

root = Tk()
root.title('Clock')
root.iconbitmap('')
# Set geometry

root.geometry("500x350")
#time
def time1():
	string = strftime('%H:%M:%S %p')
	lbl.config(text=string)
	lbl.after(1000, time)

def time_update():
    t2=threading.Thread(target=time_up,args=())
    t2.start()

def time_up():
    while (True):

        current_time = datetime.datetime.now().strftime("%H:%M:%S")
        lbl.configure(text=current_time)



# Use Threading

def Threading():
    t1 = Thread(target=alarm,args=())

    t1.start()


def alarm():
    # Infinite Loop
    global  current_time

    while True:

        # Set Alarm

        set_alarm_time = f"{hour.get()}:{minute.get()}:{second.get()}"

        # Wait for one seconds

        time.sleep(1)

        # Get current time

        current_time = datetime.datetime.now().strftime("%H:%M:%S")


        print(current_time,"alarm time=", set_alarm_time)

        # Check whether set alarm is equal to current time or not

        if current_time == set_alarm_time:
            print("Time to Wake up")

            # Playing sound
            play_alarm_sound()
            snooze = input("Press 's' to snooze for 5 minutes, or any other key to stop the alarm: ")
            if snooze.lower() == 's':
                snooze_alarm()
def play_alarm_sound():
    for i in range(0, 1):
        winsound.PlaySound("sound.wav", winsound.SND_ASYNC)
        time.sleep(4)
def snooze_alarm():
    print("Snoozing for 5 minutes...")
    time.sleep(5)  # Sleep for 5 minutes (300 seconds)
    print("Wake up!")
    play_alarm_sound()

# Add Labels, Frame, Button, Optionmenus

Label(root, text="Clock", font=("Helvetica 20 bold"), fg="red").pack(pady=10)

lbl = Label(root, font=('calibri', 40, 'bold'), foreground='black')

# Placing clock at the centre
# of the tkinter window
lbl.pack(anchor='center')
time_update()
time1()
Label(root, text="Set Time", font=("Helvetica 20 bold")).pack(pady=10)

frame = Frame(root)
frame.pack(pady=20)

hour = StringVar(root)

hours = ('00', '01', '02', '03', '04', '05', '06', '07',

         '08', '09', '10', '11', '12', '13', '14', '15',

         '16', '17', '18', '19', '20', '21', '22', '23', '24'

         )

hour.set(hours[0])

hrs = OptionMenu(frame, hour, *hours)

hrs.pack(side=LEFT)

minute = StringVar(root)

minutes = ('00', '01', '02', '03', '04', '05', '06', '07',

           '08', '09', '10', '11', '12', '13', '14', '15',

           '16', '17', '18', '19', '20', '21', '22', '23',

           '24', '25', '26', '27', '28', '29', '30', '31',

           '32', '33', '34', '35', '36', '37', '38', '39',

           '40', '41', '42', '43', '44', '45', '46', '47',

           '48', '49', '50', '51', '52', '53', '54', '55',

           '56', '57', '58', '59', '60')

minute.set(minutes[0])

mins = OptionMenu(frame, minute, *minutes)

mins.pack(side=LEFT)

second = StringVar(root)

seconds = ('00', '01', '02', '03', '04', '05', '06', '07',

           '08', '09', '10', '11', '12', '13', '14', '15',

           '16', '17', '18', '19', '20', '21', '22', '23',

           '24', '25', '26', '27', '28', '29', '30', '31',

           '32', '33', '34', '35', '36', '37', '38', '39',

           '40', '41', '42', '43', '44', '45', '46', '47',

           '48', '49', '50', '51', '52', '53', '54', '55',

           '56', '57', '58', '59', '60')

second.set(seconds[0])

secs = OptionMenu(frame, second, *seconds)

secs.pack(side=LEFT)

Button(root, text="Set Alarm", font=("Helvetica 15"), command=Threading).pack(pady=10)

# Execute Tkinter
root.mainloop()