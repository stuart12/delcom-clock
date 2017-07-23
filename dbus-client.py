#!/usr/bin/python3
# Based on http://stackoverflow.com/questions/22390064/use-dbus-to-just-send-a-message-in-python

# Python script to call the methods of the DBUS Test Server

from pydbus import SystemBus
import sys

#get the session bus
bus = SystemBus()

o2  = bus.get("org.freedesktop.DBus")


pat = "it.pook.DelcomClock."
if len(sys.argv) > 1:
    name = pat + sys.argv[1]
else:
    for n in o2.ListNames():
        if n.startswith("it.pook.DelcomClock."):
            name = n
            break
    else:
        sys.exit("no delcom")
print("anme", name)

#get the object
the_object = bus.get(name)

#call the methods and print the results
reply = the_object.Hello()
print(reply)

reply = the_object.EchoString("test 123")
print(reply)

the_object.Quit()
