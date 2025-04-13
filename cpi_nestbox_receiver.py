# CPI Nestbox Receiver
# Listens for message from nestbox monitor and notifies Raspberry Pi (nestbox logger)
#
# - Run on micro:bit receiver which is connected to the Raspberry Pi (nestbox logger) by USB
# - Prints message to Pi when radio message "occupied" is received
#   from the monitoring micro:bit located in the nesting box
#
# Note: This script will need to be flashed to the micro:bit using a tool such as:
#       https://python.microbit.org/v/3

from microbit import *
import radio

# Configure the micro:bit radio
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
