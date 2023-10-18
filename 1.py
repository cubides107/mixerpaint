import pyfirmata
import inspect  # Import the 'inspect' module

comport = 'COM10'

board = pyfirmata.Arduino(comport)

led_1 = board.get_pin('d:7:o')

# The following line is likely incorrect; you can't read a digital output pin
# a = led_1.read(0)
# print(a)

# Instead, to set the LED on, you can use:
led_1.write(0)

# To turn it off:
# led_1.write(0)