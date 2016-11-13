Mobility
========

####Libraries
We are using RPi.GPIO for basic IO
We are using https://github.com/sarfata/pi-blaster to PWM servos like https://github.com/lawsonkeith/picar

####Files
steering.py steer() takes a float between .1 and .2 (inclusive) and moves the steering servo to steer the vehicle from right (.1), left (.2) and center (.15)

####Notes
pi-blaster pwm values for rock crawler steering servo are 0.1 for right, 0.15 for center, 0.2 for left. Values in between enable steering to variable degrees. Servo steering servo voltage as sampled from the stock controller was 5.68vdc. Giving the servo 5vdc from the raspberry pi gpio headers seems to work fine without any reboots or shutdowns of the pi.
