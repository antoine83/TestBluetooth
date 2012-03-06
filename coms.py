#!/usr/bin/python
# _*_ coding: iso-8859-15 _*_

import bluetooth
import time

bd_addr = "00:40:D0:C0:A8:45"
port=1

sock=bluetooth.BluetoothSocket(bluetooth.RFCOMM)
sock.connect((bd_addr, port))
sock.send("COUCOU\r\n")

time.sleep(1)
sock.close()

