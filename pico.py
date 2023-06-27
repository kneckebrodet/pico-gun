from machine import Pin, PWM
from time import sleep

laser = Pin(15, Pin.OUT)
buzzer = PWM(Pin(17, Pin.OUT))
laser.off()
button = Pin(14, Pin.IN, Pin.PULL_DOWN)
button_pressed = False

while True:
    if button.value() and not button_pressed:
        button_pressed = True
        laser.on()
	buzzer.duty_u16(0x8000)
        sleep(0.2)
        laser.off()
	buzzer.duty_u16(0)
    if not button.value() and button_pressed:
        button_pressed = False

GPIO.cleanup()
