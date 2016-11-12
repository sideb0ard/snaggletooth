GPIO
====

####Libraries
We are using RPi.GPIO for basic IO
Potentially using https://github.com/sarfata/pi-blaster to PWM RC controllers like https://github.com/lawsonkeith/picar

####Files
helloblink.py blinks an LED to validate RPi.GPIO is installed and the pi is working correctly.
hellopwm.py fades up LEDs to validate pi-blaster is installed and is a reference script for PWM.

####Notes
pi-blaster pwm values for rock crawler steering servo are 0.1 for right, 0.15 for center, 0.2 for left. Values in between enable steering to variable degrees. Servo steering servo voltage as sampled from the stock controller was 5.68vdc. Giving the servo 5vdc from the raspberry pi gpio headers seems to work fine without any reboots or shutdowns of the pi.
