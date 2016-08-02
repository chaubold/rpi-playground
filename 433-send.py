#!/usr/bin/python3
import time
from rpi_rf import RFDevice

# read one signal from 27 (otherwise loop and check for newer timestamps)
rfdevice = RFDevice(27)
rfdevice.enable_rx()
time.sleep(0.1)
print(rfdevice.rx_code_timestamp)
print(rfdevice.rx_code)
print(rfdevice.rx_pulselength)
print(rfdevice.rx_proto)
rfdevice.cleanup()

# send lamp on, off (each 2 times just to be sure it worked)
rfdevice = RFDevice(17)
rfdevice.enable_tx()
print("Turning lamp on")
rfdevice.tx_code(333073)
rfdevice.tx_code(333073)

time.sleep(1)

print("Turning lamp off")
rfdevice.tx_code(333076)
rfdevice.tx_code(333076)

# cleanup
rfdevice.cleanup()
