import RPi.GPIO as GPIO
from time import sleep
from LCD import *
import tkinter as tk
import threading
from datetime import datetime

led_pin = 14
Buzzer_pin = 15
fan_pin = 18

# Function to initialize GPIO pins
def init_GPIO():
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(led_pin, GPIO.OUT, initial=GPIO.LOW)
    GPIO.setup(fan_pin, GPIO.OUT, initial=GPIO.LOW)
    GPIO.setup(Buzzer_pin, GPIO.OUT, initial=GPIO.LOW)

# Function to turn light ON
def Light_ON():
    GPIO.output(led_pin, GPIO.HIGH)

# Function to turn light OFF
def Light_OFF():
    GPIO.output(led_pin, GPIO.LOW)

# Function to turn buzzer ON
def Buzzer_ON():
    GPIO.output(Buzzer_pin, GPIO.HIGH)

# Function to turn buzzer OFF
def Buzzer_OFF():
    GPIO.output(Buzzer_pin, GPIO.LOW)

# Function to turn fan ON
def Fan_ON():
    GPIO.output(fan_pin, GPIO.HIGH)

# Function to turn fan OFF
def Fan_OFF():
    GPIO.output(fan_pin, GPIO.LOW)

# Function to display time on LCD
import threading
from time import sleep
from datetime import datetime

# Define a threading lock
lock = threading.Lock()

def set_time():
    global continue_display
    continue_display = True
    def display_time():
        while continue_display:
            # Get current date and time
            current_time = datetime.now()
            # Format current time
            formatted_time = current_time.strftime("%H:%M:%S")
            formatted_time = "Time: {}".format(formatted_time)
            # Acquire lock before accessing shared resource (lcd_string)
            with lock:
                lcd_string(formatted_time, 1)
            sleep(1)
    threading.Thread(target=display_time).start()

def set_alarm():
    lcd_string(" Setting Alarm", LCD_LINE_1)
    sleep(1)

    # Get the input values for alarm hour and minute
    alarm_hour_str = alarm_Entry_hr.get()
    alarm_minute_str = alarm_Entry_min.get()
    
    # Check if the input values are not empty
    if alarm_hour_str and alarm_minute_str:
        # Convert input values to integers
        alarm_hour = int(alarm_hour_str)
        alarm_minute = int(alarm_minute_str)

        current_time = datetime.now()
        current_hour = current_time.hour
        current_minute = current_time.minute
        
        # Calculate the remaining time until the alarm
        if alarm_hour > current_hour or (alarm_hour == current_hour and alarm_minute >= current_minute):
            hour_diff = alarm_hour - current_hour
            minute_diff = alarm_minute - current_minute
            if minute_diff < 0:
                hour_diff -= 1
                minute_diff += 60
            lcd_string("Alarm in", LCD_LINE_1)
            lcd_string(f"{minute_diff} min", LCD_LINE_2)
        else:  # this code is for if time less than required time means will calculate for tomorrow
            hour_diff = 24 - (current_hour - alarm_hour)
            minute_diff = alarm_minute - current_minute
            if minute_diff < 0:
                minute_diff += 60
            lcd_string("Alarm in", LCD_LINE_1)
            lcd_string(f"{hour_diff} hr {minute_diff} min", LCD_LINE_2)
        
        # Calculate total time to sleep in milliseconds (root.after() takes time in milliseconds)
        time_to_sleep = 1000 *60 *(60 * hour_diff + minute_diff) #time to sleep is in ms
        
        # Schedule turning on the buzzer after the alarm time has elapsed
        root.after(time_to_sleep, Buzzer_ON_and_off)
    else:
        # Handle case where input values are empty
        lcd_string("Invalid input", LCD_LINE_1)

def Buzzer_ON_and_off():
    Buzzer_ON()  # Turn on the buzzer
    # Schedule turning off the buzzer after 5 seconds
    root.after(5000, Buzzer_OFF)



		
# Initialize GPIO pins
init_GPIO()
# Initialise display
lcd_init()

# Tkinter setup
root = tk.Tk()
root.title("Smart Home")
root.geometry("400x300")
root.config(bg="#202124")  # Dark mode background color

# Frame for input fields
input_frame = tk.Frame(root, bg="#202124")  # Dark mode background color
input_frame.pack(pady=10)

# Label and button for Light
light_label = tk.Label(input_frame, text="Light:", bg="#202124", fg="white")  # Dark mode colors
light_label.grid(row=0, column=0, padx=5, pady=5)

LON_button = tk.Button(input_frame, text="ON", command=Light_ON, bg="#757575", fg="white")  # Dark mode colors
LON_button.grid(row=0, column=1, padx=5, pady=5)

LOFF_button = tk.Button(input_frame, text="OFF", command=Light_OFF, bg="#757575", fg="white")  # Dark mode colors
LOFF_button.grid(row=0, column=2, padx=5, pady=5)

# Label and button for Fan
fan_label = tk.Label(input_frame, text="Fan:", bg="#202124", fg="white")  # Dark mode colors
fan_label.grid(row=1, column=0, padx=5, pady=5)

FON_button = tk.Button(input_frame, text="ON", command=Fan_ON, bg="#757575", fg="white")  # Dark mode colors
FON_button.grid(row=1, column=1, padx=5, pady=5)

FOFF_button = tk.Button(input_frame, text="OFF", command=Fan_OFF, bg="#757575", fg="white")  # Dark mode colors
FOFF_button.grid(row=1, column=2, padx=5, pady=5)

# Label and button for Time
time_label = tk.Label(input_frame, text="Current Time:", bg="#202124", fg="white")  # Dark mode colors
time_label.grid(row=2, column=0, padx=5, pady=5)

time_button = tk.Button(input_frame, text="Display Time", command=set_time, bg="#757575", fg="white")  # Dark mode colors
time_button.grid(row=2, column=1, padx=5, pady=5)

#label, entry and button for alarm
alarm_label = tk.Label(input_frame, text="Alarm config:", bg="#202124", fg="white")  # Dark mode colors
alarm_label.grid(row=3, column=0, padx=5, pady=5)

alarm_label = tk.Label(input_frame, text="Hr", bg="#202124", fg="white")  # Dark mode colors
alarm_label.grid(row=4, column=0, padx=5, pady=5)

alarm_Entry_hr = tk.Entry(input_frame, width=10, bg="#757575", fg="white")  # Dark mode colors
alarm_Entry_hr.grid(row=4, column=1, padx=1, pady=1)

alarm_label = tk.Label(input_frame, text="Min", bg="#202124", fg="white")  # Dark mode colors
alarm_label.grid(row=4, column=2, padx=5, pady=5)

alarm_Entry_min = tk.Entry(input_frame, width=10, bg="#757575", fg="white")  # Dark mode colors
alarm_Entry_min.grid(row=4, column=3, padx=1, pady=1)

alarm_button = tk.Button(input_frame, text="Set Alarm", command=set_alarm, bg="#757575", fg="white")  # Dark mode colors
alarm_button.grid(row=5, column=1, padx=5, pady=5)

# Function to clean up GPIO pins and exit the application
def clean_up():
    global continue_display
    continue_display = False
    GPIO.cleanup()
    root.destroy()

# Button to exit application
exit_button = tk.Button(root, text="Exit", command=clean_up, bg="#757575", fg="white")  # Dark mode colors
exit_button.pack(pady=10)

root.mainloop()
