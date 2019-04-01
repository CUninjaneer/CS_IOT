import RPi.GPIO as GPIO  
import time  

pin = 8
interval = 0.1
total_time = 5
cycles = int(total_time/(2*interval))

def blink(pin):  
    GPIO.output(pin,GPIO.HIGH)  
    time.sleep(interval)  
    GPIO.output(pin,GPIO.LOW)  
    time.sleep(interval)  
    return  

GPIO.setmode(GPIO.BOARD)  

GPIO.setup(pin, GPIO.OUT)  

for i in range(0,cycles):  
    blink(pin)  

GPIO.cleanup() 
