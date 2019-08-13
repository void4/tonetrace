from time import sleep
from audio import on, off
import sys

def tracefunc(frame, event, arg, indent=[0]):
	if event == "call":
		indent[0] += 2
		print("-" * indent[0] + "> call function", frame.f_code.co_name)
		on(50 + 1*indent[0])
		sleep(0.1)
	elif event == "return":
		print("<" + "-" * indent[0], "exit function", frame.f_code.co_name)
		off(50 + 1*indent[0])
		indent[0] -= 2

	return tracefunc

def trace():
	#sys.settrace(tracefunc)
	sys.setprofile(tracefunc)
