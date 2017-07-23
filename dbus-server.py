#!/usr/bin/python3
#https://github.com/LEW21/pydbus/blob/master/examples/clientserver/server.py
import sys
import time
import math
import random
from gi.repository import GLib
try:
    from pydbus import SystemBus
except ImportError:
    sys.exit("sudo apt-get install python3-pydbus")

loop = GLib.MainLoop()

def timeout(arg):
    start = time.time()
    time.sleep(random.uniform(0.001, 0.5))
    now = time.time()
    mf = math.modf(time.time())
    decimals = mf[0]
    delay = 1 - decimals
    print(arg, start, now, mf, decimals, delay)

    GLib.timeout_add(math.ceil(delay * 1000 ), timeout, arg)
    return False

class MyDBUSService(object):
	"""
		<node>
			<interface name='it.pook.DelcomClock.control'>
				<method name='Hello'>
					<arg type='s' name='response' direction='out'/>
				</method>
				<method name='EchoString'>
					<arg type='s' name='a' direction='in'/>
					<arg type='s' name='response' direction='out'/>
				</method>
				<method name='Quit'/>
			</interface>
		</node>
	"""

	def Hello(self):
		"""returns the string 'Hello, World!'"""
		return "Hello, World!"

	def EchoString(self, s):
		"""returns whatever is passed to it"""
		return s

	def Quit(self):
		"""removes this object from the DBUS connection and exits"""
		loop.quit()

random.seed()
bus = SystemBus()
name = sys.argv[1]
bus.publish("it.pook.DelcomClock." + name, MyDBUSService())
bus.publish("it.pook.DelcomClock." + "wooble", MyDBUSService())
GLib.timeout_add(100, timeout, "foo")
loop.run()
