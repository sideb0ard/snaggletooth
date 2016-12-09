pin0 = 4
pwmDev = open('/dev/pi-blaster', 'w')

def steer(pwmVal):
    pwmVal = float(pwmVal)
    if pwmVal >= 0.1 and pwmVal <= 0.2:
        pwmDev.write('%d=%s\n'%(pin0, str(pwmVal)))
    else:
        print("No thanks: pwmVal was not a float between .1 and .2")
    print("pwmVal = {}".format(pwmVal))

def left():
    steer(0.2)

def right():
    steer(0.1)

def center():
    steer(0.15)

if __name__ == "__main__":
    import sys

    def cliSteer():
        steer(sys.argv[2])

    cliFunctions = {"left":left,"right":right,"center":center,"steer":cliSteer}
    try:
        cliFunctions[sys.argv[1]]()
    except:
        print("No thanks: Missing or invalid arguments.")
