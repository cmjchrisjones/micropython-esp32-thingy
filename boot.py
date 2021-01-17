import micropython
import webrepl
import esp
import os

os.listdir()

esp.osdebug(None)

webrepl.start()

micropython.opt_level(2)
