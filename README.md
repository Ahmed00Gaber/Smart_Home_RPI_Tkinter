# Smart Home Controller

This Python script is designed to control various devices connected to a Raspberry Pi, such as LED lights, a buzzer, and a fan. The project provides a graphical user interface (GUI) built using the Tkinter library to interact with these devices.

## Features

- **Light Control:** Users can turn the LED light ON and OFF using dedicated buttons.

- **Fan Control:** Users can turn the fan ON and OFF using dedicated buttons.

- **Time Display:** Users can display the current time on an LCD screen.

- **Alarm Configuration:** Users can set an alarm by specifying the hour and minute. The script will calculate the remaining time until the alarm and trigger a buzzer when the alarm time is reached.

## Dependencies

- RPi.GPIO
- Tkinter
- LCD module (Assumed to be provided as `LCD.py`)

## Usage

To use the Smart Home Controller:

1. Make sure you have Python installed on your Raspberry Pi.
2. Connect the LED, buzzer, fan, and LCD display to the Raspberry Pi.
3. Run the Python script `smart_home_controller.py`.
4. The graphical user interface will appear, allowing you to interact with the connected devices.

## GPIO Pins

- LED pin: 14
- Buzzer pin: 15
- Fan pin: 18


