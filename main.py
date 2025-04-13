# CPI Nestbox Receiver
#
# Run on a micro:bit controller (which is connected to the Raspberry Pi by USB)
# Sends a signal to the Pi when radio message "occupied" is received from the Monitor script

from microbit import *
import radio

# Configure the radio
radio.on()
radio.config(group=42)

# Listen for the radio message 'occupied'.
# If it is received, print a confirmation message to the Rasperry Pi (over USB connection)
while True:
    msg = radio.receive()  # Listen for message
    if msg == "occupied":
        display.show("O")
        print("occupied")  # Send message to Raspberry Pi over USB
        sleep(2000)  # Pause before clearing
        display.clear()
    sleep(100)  # Pause before checking for radio message again
