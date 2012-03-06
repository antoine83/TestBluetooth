#!/usr/bin/python
# _*_ coding: iso-8859-15 _*_

import bluetooth

print "BT scanning..."
btdevices = bluetooth.discover_devices(flush_cache=True)
for bdaddr in btdevices:
	print bdaddr+" : "+bluetooth.lookup_name(bdaddr)
	services = bluetooth.find_service(address=bdaddr)
	for svc in services:
		print "    - %s" % svc["name"]


