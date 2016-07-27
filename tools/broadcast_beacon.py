#!/usr/bin/env python

# Info from:
# http://yencarnacion.github.io/eddystone-url-calculator/ and
# https://hackaday.io/project/10314-raspberry-pi-3-as-an-eddystone-url-beacon

import sys
import subprocess


def encodeUrl(url):
    # see links in header for details of these fields
    prefix = "0x08 0x0008 17 02 01 06 03 03 aa fe 0f 16 aa fe 10 00 02 "
    print "I got yer url:{0}".format(url)
    url = url.encode("hex")
    if len(url) > 34:
        print "Yer URL is too long mate"
        exit(1)
    print url
    print len(url)

    while len(url) < 34:
        url = url + "00"

    print len(url)

    url = " ".join(url[i:i + 2] for i in range(0, len(url), 2))
    output = prefix + url

    ip = subprocess.check_output(["/sbin/ifconfig wlan0 | grep 'inet addr' | "
                                  "awk '{print $2}' | sed 's/addr://'"])

    print "IP: {0}".format(ip)
    print "Output: {0}".format(output)


if __name__ == "__main__":
    if len(sys.argv) == 2:
        print "Yarly!"
        encodeUrl(sys.argv[1])
    else:
        print "boo"
