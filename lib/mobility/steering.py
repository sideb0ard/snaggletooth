pin0 = 4
pwmDev = open('/dev/pi-blaster', 'w')

def steer(pwmVal):
    pwmVal = float(pwmVal)
    if pwmVal >= 0.1 and pwmVal <= 0.2:
        pwmDev.write('%d=%s\n'%(pin0, str(pwmVal)))
    else:
        print("pwmVal was not a float between .1 and .2")
    print("pwmVal = {}".format(pwmVal))

if __name__ == "__main__":
    import sys
    steer(float(sys.argv[1]))
