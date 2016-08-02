# Controlling RC-switches via the raspberry pi

Using the python package rpi-rf (installed via pip3).
Needed to replace `time.perf_counter()` by `time.time()`.

Use the following to scan all signals that are passing by:

```
sudo rpi-rf_receive
```

To send, e.g. ON and OFF for D in our home:

```
# ON
sudo rpi-rf_send 333073
# OFF
sudo rpi-rf_send 333076
```

See images for how they are connected, or see
tutorials-raspberrypi.de/raspberry-pi-funksteckdosen-433-mhz-steuern