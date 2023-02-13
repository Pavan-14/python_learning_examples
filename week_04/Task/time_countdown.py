""" The goal of the task is to create a Countdown timer application.
    the required modules to complete the task:
    1. time for sleep()
    2. tkinter module used to create GUI of application and also to display messagebox """

import time
from tkinter import *
from tkinter import messagebox


class TimeCountdown:
    """ the class useful to create countdown time """
    # constructor
    def __init__(self):
        
        # Application window configurations
        self.display = Tk()
        self.display.title("Timer App")
        self.display.geometry("500x500")
        self.display.config(bg="light green")


        # create a entry widget
        # variable to store enter value
        self.time_value = StringVar()
        self.time_entry = Entry(self.display, textvariable=self.time_value, font=("Calibri", 20))
        self.time_entry.grid(row = 0, column = 1, columnspan=3, padx = 5, pady = 5)

        # create a start button
        self.start_button = Button(self.display, font=("Calibri", 12), text="Start", relief=RAISED, command=self.start)
        self.start_button.grid(row = 0, column = 4, padx = 3, pady = 3)

        # create a stop button
        self.stop_button = Button(self.display, font=("Calibri", 12), text="Stop", relief=RAISED, command=self.stop)
        self.stop_button.grid(row = 0, column = 5, padx = 3, pady = 3)

        # create a label to show timer time
        self.timer_label = Label(self.display, font=("Calibri", 12), text="Time: 00:00:00", bg="light green")
        self.timer_label.grid(row = 2, column = 1, padx = 3, pady = 3)

        self.stop_loop = False

        self.display.mainloop()
    

    # start button command function
    def start(self):

        self.stop_loop = False

        seconds, minutes, hours = 0, 0, 0

        
        get_time = self.time_value.get().split(":")
        print(get_time)
        
        # if the input like 1:2:10
        if len(get_time) == 3:
            seconds = int(get_time[2])
            minutes = int(get_time[1])
            hours = int(get_time[0])

       # if the input like 2:10
        elif len(get_time) == 2:
            seconds = int(get_time[1])
            minutes = int(get_time[0])

        # if the input like 456789
        elif len(get_time) == 1:
            seconds = int(get_time[0])
        else:
            print("Invallid time Format")
       
        # convert the time into seconds
        time_in_seconds = hours * 3600 + minutes * 60 + seconds
        print(time_in_seconds)
        messagebox.errorinfo("Error","Enter time in 00:00:00 or 5689 format")
        
        # update the timer every 1 second
        while time_in_seconds > 0 and not self.stop_loop:
            time_in_seconds -= 1
            minutes, seconds = divmod(time_in_seconds, 60)
            hours, minutes = divmod(minutes, 60)
            self.timer_label.config(text=f"Time: {hours:02}:{minutes:02}:{seconds:02}", font=("Calibri", 30), fg="red")
            self.display.update()
            time.sleep(1)

        # To dispaly Time's Up message
        if not self.stop_loop:
            self.time_entry.delete(0,END)
            messagebox.showinfo("timeout","Time is up!")

    def stop(self):
        self.stop_loop = True
        self.timer_label.config(text="Timer: 00:00:00")
        self.time_entry.delete(0,END)

        
# class object/Instance
TimeCountdown()
