# 🐙 ESP32C3 Supermini – MicroPython Examples (octopusLAB Framework)

A collection of MicroPython examples and utilities for the **ESP32C3 Supermini Development Board**, built on top of the [octopusLAB MicroPython Framework](https://github.com/octopuslab-cz/esp32_micropython_framework).
Demonstrates how to initialize hardware, control peripherals, run example scripts for LEDs, I2C, SPI, and more.

---

## 💻 Environment

We use [**Thonny IDE**](https://thonny.org/) for developing, flashing, and running MicroPython code directly on the ESP32 board.

Thonny allows:
- simple USB connection to MicroPython devices,
- firmware installation and update,
- direct execution and editing of scripts.

---

## ⚙️ 1) Installing MicroPython on ESP32C3

In **Thonny IDE**:

1. Open menu: **Run → Configure Interpreter**
2. Select interpreter type: **MicroPython (ESP32)**
3. Click **Install or Update MicroPython**
4. Choose the correct serial port - e.g. `/dev/ttyUSB0` (for Linux) or `COMx` (Windows)
5. Confirm installation and wait for flashing to complete

After installation, open the **Shell** — you should see the MicroPython prompt `>>>`.

---

## 🧰 2) Installing the octopusLAB Framework

Connect the ESP32C3 board to Wi-Fi and install the framework using `mip`:

```python
from time import sleep
import network
import mip

wlan = network.WLAN(network.STA_IF)
wlan.active(True)
sleep(5)

print("wifi connect")
wlan.connect('ssid', 'password')
sleep(5)

mip.install("github:octopuslab-cz/esp32_micropython_framework/package_min.json", target=".")
```

---

# ESP32C3 Supermini – octopusLAB MicroPython Framework


## 🧰 Requirements

- ESP32C3 Supermini board (USB-C version)
- [Thonny IDE](https://thonny.org/)
- [MicroPython firmware](https://micropython.org/download/esp32c3/)
- octopusLAB MicroPython Framework

## ⚙️ Setup

1. **Flash MicroPython** firmware to your ESP32C3 board.
2. Open **Thonny IDE** and select your serial port.
3. In Thonny’s **Tools → Options → Interpreter**, choose “MicroPython (ESP32)”.  
4. Clone or copy the octopusLAB Framework to your board:
   ```python
   import mip
   mip.install("github:octopuslab-cz/esp32_micropython_framework")
   ```
5. Configure your device:
   ```python
   setup()  # in ds (device setup) menu
   ```
   It is assumed that you have configured the ESP32C3mini board using **setup()** in the **ds (device setup)** menu, which provides access to the declared pinout.

---

## 💡 Examples

### Blink LED
```python
from utils.pinout import set_pinout
from components.led import Led

pinout = set_pinout()
led = Led(pinout.BUILT_IN_LED)

for blink in range(3):
    led.value(0)
    sleep_ms(500)
    led.value(1)
    sleep_ms(500)

"""
while True:
    led.toggle()
    sleep_ms(500)
"""
```

### Read Button
```python
from machine import Pin

button = Pin(9, Pin.IN, Pin.PULL_UP)
print("Button pressed:", not button.value())
```

### I2C setup | test
```python
from octopus_lib import i2c_init
i2c = i2c_init()
print(i2c.scan())
```

## 📁 Folder Structure

```
  
  ├── component/
  ├── config/
  ├── examples/
  ├── config/
  ├── lib/
  ├── pinouts/
  └── utils/
  /main.py
```

## 🧩 Notes

- Tested on **ESP32C3 Supermini (Ai-Thinker)**.
- Compatible with **octopusLAB Framework v1.9+**.
- Examples can be executed directly from Thonny.

---

## 🪴 Author & License

Created by **octopusLAB community**  
Licensed under **MIT License**  
More info: [github.com/octopuslab-cz](https://github.com/octopuslab-cz)
