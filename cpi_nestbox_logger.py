# CPI Raspberry Pi Logger
#
# - Listens for signal from nestbox receiver via usb serial port signal.
# - Logs date/time to log file.
# - Log file is read by web page which periodically auto-refreshes

import serial
from datetime import datetime

# Use `ls /dev/ttyACM*` to find address of USB serial port if unknown
SERIAL_PORT = '/dev/ttyACM0'
BAUD_RATE = 115200
LOG_FILE = '/var/www/html/baaak/nestbox_status.txt'

# Open the serial connection
with serial.Serial(SERIAL_PORT, BAUD_RATE, timeout=1) as ser:
    print("Listening for nesting box status...")
    while True:
        line = ser.readline().decode('utf-8').strip()
        if line:
            if line == "occupied":
                timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                # Print to console
                print(f"[{timestamp}] Nestbox occupied")
                # Write to the log file
                with open(LOG_FILE, 'w') as f:
                    f.write(f"Nest box occupied: {timestamp}\n")