#!/usr/bin/env python

# Info from:
# http://yencarnacion.github.io/eddystone-url-calculator/ and
# https://hackaday.io/project/10314-raspberry-pi-3-as-an-eddystone-url-beacon

import os
import sys
import subprocess


def sendBeacon():

    uid =  os.getuid()
    if uid != 0:
	print "Sorry, pal, need to be superuser to change hci settings"
	exit(1)

    ip = subprocess.check_output("/sbin/ifconfig wlan0 | grep 'inet addr' | "
                                 "awk '{print $2}' | sed 's/addr://'",
				 shell=True)
    ip = ip.rstrip('\n')

    ## see links in header for details of these fields
    prefix = "0x08 0x0008 17 02 01 06 03 03 aa fe 0f 16 aa fe 10 00 02 "
    url = ip.encode("hex")
    if len(url) > 34:
        print "Yer URL is too long mate"
        exit(1)

    while len(url) < 34:
        url = url + "00"

    url = " ".join(url[i:i + 2] for i in range(0, len(url), 2))
    encoded_params = prefix + url

    print "{0}".format(encoded_params)

    print "Putting hci0 in broadcast mode..."
    subprocess.check_call(["hciconfig", "hci0", "reset"])
    subprocess.check_call(["hciconfig", "hci0", "leadv", "3"])

    cmd = "hcitool -i hci0 cmd " + encoded_params
    subprocess.check_output(cmd, shell=True) 


if __name__ == "__main__":
    sendBeacon()
