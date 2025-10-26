# (c) OctopusLAB 2016-25 - MIT
#  3x i2c setup

from machine import Pin, I2C

# --------------------------------- 1
print("[--- init1 ---] Pin")
# HW or SW: HW 0 - | SW -1
# freq=f
i2c = I2C(scl=Pin(9), sda=Pin(8))
print(i2c.scan())

# --------------------------------- 2
print("[--- init2 ---] pinout")
from utils.pinout import set_pinout
pinout = set_pinout()

print(pinout.I2C_SCL_PIN,pinout.I2C_SDA_PIN)
i2c = I2C(scl=Pin(pinout.I2C_SCL_PIN), sda=Pin(pinout.I2C_SDA_PIN))

# --------------------------------- 3
print("[--- init3 ---] lib")

from octopus_lib import i2c_init
i2c = i2c_init()
print(i2c.scan())

"""
It is assumed that you have configured the ESP32C3mini board: using setup()
in the ds (device setup) menu, which provides access to the declared pinout
"""