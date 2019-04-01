################################################################################
# The Raspberry Pi Platform and Python Programming for the Raspberry Pi
# Course 4 in the IoT Specialization
# Module 4
# Assignment 1
# Adam Britt
# March 31, 2019
################################################################################
# Problem Statement:
#
# Build a circuit using your Raspberry Pi that causes an LED to blink when a
# push button is NOT pressed. However, the LED should stay on continually when
# the push button IS pressed.
#
# Your video should show the LED blinking when the push button is not pressed,
# and it should show that the LED is constantly on while the button is pressed.
#
# Take a video of your circuit in action and submit a hyperlink to your video.
# Do not upload a video here.
################################################################################
import RPi.GPIO as GPIO
import time

led_pin = 8
interval = 0.1
total_time = 10
cycles = int(total_time/(2*interval))
button_pin_in = 11
quit_pin_in = 13

def blink(led_pin):
    GPIO.output(led_pin,GPIO.HIGH)
    time.sleep(interval)
    GPIO.output(led_pin,GPIO.LOW)
    time.sleep(interval)
    return

def steady(led_pin):
    GPIO.output(led_pin,GPIO.HIGH)
    time.sleep(2*interval)
    return

GPIO.setmode(GPIO.BOARD)
GPIO.setup(led_pin, GPIO.OUT)
GPIO.setup(button_pin_in, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(quit_pin_in, GPIO.IN, pull_up_down=GPIO.PUD_UP)

start = time.time()
while True:
    quit_check = GPIO.input(quit_pin_in)
    blink_button = GPIO.input(button_pin_in)
    if quit_check == 0:
        break
    elif blink_button == 0:
        steady(led_pin)
    else:
        blink(led_pin)
finish = time.time()
elapsed = finish - start
print ("Elapsed time of %f seconds" %  elapsed)
GPIO.cleanup()
