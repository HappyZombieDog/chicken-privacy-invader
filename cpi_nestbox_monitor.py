# CPI Nestbox Monitor
# Monitors the occupancy of the nestbox
#
# - Run on micro:bit controller located in the nestbox
# - When the nestbox is occupied (circuit connecting pins 1 and GND is closed),
#   sends radio message 'occupied' (which is picked up by the Receiver micro:bit)
#
# Note: This script will need to be flashed to the micro:bit using a tool such as:
#       https://python.microbit.org/v/3


from microbit import *
import radio

# Configure the micro:bit radio
radio.on()
radio.config(group=42)

# Configure micro:bit pin0
pin0.set_pull(pin0.PULL_UP)  # Set internal pull-up resistor

# Repeatedly read pin0 to check whether circuit is closed (indicating nestbox is occupied)
# If circuit is closed, send the radio signal
while True:
    if pin0.read_digital() == 0:  # Circuit connected
        radio.send("occupied")
        # Enable the lines below for visual debugging; Comment them out to conserve battery power.
        # display.show("E")
        # sleep(5000)
        # display.clear()
    sleep(100)
