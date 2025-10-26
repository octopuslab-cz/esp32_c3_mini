# (c) OctopusLAB 2016-25 - MIT

from time import sleep_ms
from machine import Pin

print("[--- init ---] pinout")

led = Pin(8, Pin.OUT)

for blink in range(3):
    led.value(1)
    sleep_ms(500)
    led.value(0)
    sleep_ms(500)


print("[--- pause ---] 3s")
sleep_ms(3000)
# =================================

from utils.pinout import set_pinout
from components.led import Led

print("[--- simple init ---] pinout")
pinout = set_pinout()

print("[--- simple init ---] led")
led = Led(pinout.BUILT_IN_LED) # 2

print("[--- test ---] blink 3x")
for blink in range(6):
    led.toggle()
    sleep_ms(500)

print("[-- finish --]\n")
