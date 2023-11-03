
import time
from bmp280 import BMP280
from smbus2 import SMBus

# Initialise the BMP280
bus = SMBus(1)
bmp280 = BMP280(i2c_dev=bus)

while True:
    temperature = bmp280.get_temperature()
    pressure = bmp280.get_pressure()
    print(f'{temperature}*C {pressure}hPa')
    time.sleep(1)
