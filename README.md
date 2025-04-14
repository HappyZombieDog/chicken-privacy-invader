## 🐔 CPI - The Chicken Privacy Invader ("Check in on your chooks!")

Monitor a chicken nesting box in real time to see if a chicken is nesting on it. Update local wifi network webpage 
with date and time of nestbox occupancy. Why wander out in the wind and rain to see if your chook has been on the nest? 
Stay up to date on any device on your network that has a web browser!

### Requirements
- 2 micro:bit controllers
  - Monitor (requires battery pack)
  - Receiver (powered via usb connection to the Raspberry Pi)
- 1 Raspberry Pi (logger and web server)
  - configured as a web server on your local network (set-up and configuration of
  the web server is not in the scope of this project)
- 1 USB cable (to connect the receiver micro:bit to the Raspberry Pi)
- 1 piece of cardboard sized to fit in the nesting box when folded in half (underneath the cover and wood shavings etc that the chicken
will sit on)
- 2 pieces of tin foil
- Tape or glue to attach the foil to the insides of the folded cardboard
- 2 alligator clip wires (each with clips on both ends)
- 2 ziploc bags (1 for the cardboard contact plate and 1 for the monitor micro:bit)

### Details
The system involves 2 micro:bit controllers and 1 Raspberry Pi. There is a piece of cardboard folded in half with a 
piece of tinfoil attached to each side. Each piece of tin foil is connected to the transmitting micro:bit controller by 
an alligator clip wire, one clip connecting to the GND pin and one connected to PIN0. The micro:bit transmitter sends
a radio signal to the second micro:bit (the receiver), which is in turn connected to the Raspberry Pi by USB. When the
receiving micro:bit receives a radio signal from the transmitting micro:bit, it instructs the Rasperry Pi to write 
the date and time to a log file. The Raspberry Pi is located on the local wifi network and acts as a web server. It 
serves a page on the local network which reads the log file and outputs the date-time values to the web page. The web 
page auto refreshes evry 3 minutes.
