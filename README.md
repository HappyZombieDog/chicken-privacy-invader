## CPI - The Chicken Privacy Invader

This project is about monitoring a chicken nesting box to see if a chicken is nesting in it. The system involves 
2 micro:bit controllers and 1 Raspberry Pi. There is a piece of cardboard folded in half with a piece of tinfoil 
attached to each side. Each piece of tin foil is connected to the transmitting micro:bit controller by an alligator clip
wire, one clip connecting to the GND pin and one connected to PIN0. The micro:bit transmitter sends
a radio signal to the second micro:bit (the receiver), which is in turn connected to the Raspberry Pi by USB. When the
receiving micro:bit receives a radio signal from the transmitting micro:bit, it instructs the Rasperry Pi to write 
the date and time to a log file. The Raspberry Pi is located on the local wifi network and acts as a web server. It 
serves a page on the local network which reads the log file and outputs the date-time values to the web page. The web 
page auto refreshes evry 3 minutes.
