# import necessary modules for pin control and timing
from machine import Pin
from utime import sleep_us

# define the GPIO pin for the STEP signal and set it as an output
step_pin = Pin(0, Pin.OUT)

# define the GPIO pin for the DIR (direction) signal and set it as an output
dir_pin = Pin(1, Pin.OUT)

# define the GPIO pin for the built-in LED and set it as an output
led_pin = Pin(25, Pin.OUT)  # GPIO 25 is usually the built-in LED on the Pico

# set the direction of the motor by writing a low signal to the DIR pin
dir_pin.low()

# main loop to continuously step the motor and toggle the LED
while True:
    # send a high signal to the step pin to step the motor
    step_pin.high()
    # turn the LED on
    led_pin.high()
    # pause to control the speed of the motor
    sleep_us(500)  # pause for 500 microseconds
    # send a low signal to the step pin to complete the step cycle
    step_pin.low()
    # turn the LED off
    led_pin.low()
    # pause again to maintain the step speed
    sleep_us(500)  # pause for 500 microseconds
