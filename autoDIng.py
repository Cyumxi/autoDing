from cgitb import reset
from distutils.log import error
from adbutils import adb
from time import sleep
from ppadb.client import Client as AdbClient
import os
import sys


package = "com.alibaba.android.rimet"


def raiseWake(device, password=None):
    device.keyevent("KEYCODE_WAKEUP")
    sleep(1)
    device.swipe(1200, 2800, 1200, 200)
    sleep(1)

    if password:
        # device.shell(f"input text {password}")
        device.send_keys(f"{password}")
        device.keyevent("KEYCODE_ENTER")

def detect_emulator_status(serial):
    devices = adb.device_list()
    for device in devices:
        if device.serial == serial:
            return "device"
    return 'offline'

def connectDevice(serial):
    
    if detect_emulator_status(f"{serial}") == "device":


        # client.remote_connect("1C031FDEE007VD", 5555)
        # adb.connect(f"{serial}")
        device = adb.device(f"{serial}")
        
        return device
        # print(device.)
        # device.shell("echo 233")
    else:
        adb.connect(f"{serial}")
        device = adb.device(f"{serial}")
        return device
        




# Default is "127.0.0.1" and 5037

device = connectDevice("R52R208TYKH")



# raiseWake(device, "2333")

# device.app_start("com.alibaba.android.rimet")

# sleep(2)

result = device.screenshot()
result.show()
with open("screen.png", "wb") as fp:
    result.save(fp)

