#Pin Connections:
#CSL -> GPIO3
#SDA -> GPIO2


temp_press_sensor = None

try:
    from bmp280 import BMP280
    from smbus2 import SMBus

    bus = SMBus(1)
    temp_press_sensor = BMP280(i2c_dev=bus)

except ImportError:
    print("cant import modules for bmp280")




def get_temperature():
    if (temp_press_sensor):
        return temp_press_sensor.get_temperature()
    else:
        return 0


def get_pressure():
    if (temp_press_sensor):
        return temp_press_sensor.get_pressure()
    else:
        return 0


# while True:
#     temperature = temp_press_sensor.get_temperature()
#     pressure = temp_press_sensor.get_pressure()
#     print(f'{temperature}*C {pressure}hPa')
#     time.sleep(1)
