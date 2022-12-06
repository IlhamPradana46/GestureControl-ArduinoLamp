import pyfirmata

com = "COM3"

board = pyfirmata.Arduino(com)

led_1 = board.get_pin('d:8:o')
led_2 = board.get_pin('d:9:o')
led_3 = board.get_pin('d:10:o')
led_4 = board.get_pin('d:11:o')
led_5 = board.get_pin('d:12:o')

led_1.write(0)
led_2.write(0)
led_3.write(0)
led_4.write(0)
led_5.write(0)

def ledActivate(finger):
    if finger[0] == 1:
        led_1.write(1)
    else :
        led_1.write(0)
    if finger[1] == 1:
        led_2.write(1)
    else :
        led_2.write(0)
    if finger[2] == 1:
        led_3.write(1)
    else :
        led_3.write(0)
    if finger[3] == 1:
        led_4.write(1)
    else :
        led_4.write(0)
    if finger[4] == 1:
        led_5.write(1)
    else :
        led_5.write(0)
    