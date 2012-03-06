#!/usr/bin/python
# _*_ coding: iso-8859-15 _*_

import bluetooth
import time

#*********************************************************
# http://people.csail.mit.edu/albert/bluez-intro/c212.html
#
#*********************************************************

target_name = "Antoine Faddi"
target_address = None

nearby_devices = bluetooth.discover_devices()

for bdaddr in nearby_devices:
    if target_name == bluetooth.lookup_name( bdaddr ):
        target_address = bdaddr
        break

if target_address is not None:
    print "found target bluetooth device with address ", target_address
else:
    print "could not find target bluetooth device nearby"

