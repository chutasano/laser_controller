# thanks to www.cs.uml.edu/~cgao

import smbus
import sys
import getopt
import time 
import pigpio

servos = [23, 24]
u = 1.2
x = 600
y = 1900

limit_y_bottom = 1900
limit_y_top = 1300
limit_y_level = 1900
limit_x_left = 600
limit_x_right = 2400

pi = pigpio.pi()

def head(y):
    while y > limit_y_top:
        pi.set_servo_pulsewidth(servos[1], int(y))
        print("Servo {} {} micro pulses".format(servos,y))
        time.sleep(u)
        temperature()
        y -= 300

    while y < limit_y_bottom:
        pi.set_servo_pulsewidth(servos[1], int(y))
        print("Servo {} {} micro pulses".format(servos,y))
        time.sleep(u)
        temperature()
        y += 300

    while y > limit_y_level:
        pi.set_servo_pulsewidth(servos[1], 2000)
        print("Servo {} {} micro pulses".format(servos,y))
        time.sleep(u)
        y -= 300
        
try:
    while True:
        while x < limit_x_right:
            pi.set_servo_pulsewidth(servos[0], int(x))
            print("Servo {} {} micro pulses".format(servos,x))
            time.sleep(u)
            x += 450
            head(y)
            

        while x > limit_x_left:
            pi.set_servo_pulsewidth(servos[0], int(x))
            print("Servo {} {} micro pulses".format(servos,x))
            time.sleep(u)
            x -= 450
            head(y)
 

except KeyboardInterrupt:
    for s in servos:
        pi.set_servo_pulsewidth(s, 0)

pi.i2c_close(handle)
pi.stop()


