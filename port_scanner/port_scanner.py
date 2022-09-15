#!/bin/python3

#Import modules
import sys
import socket
from datetime import datetime as dt

#Define target
if len(sys.argv) == 2:
	target = socket.gethostbyname(sys.argv[1])
else :
	print("Two arguments are required.")
	print("Syntax: python3 scanner.py <ip>")
	sys.exit() 

#Add a pretty banner
print("-" * 50)
print("Scanning port "+target)
print("Time started: "+str(dt.now()))
print("-" * 50)

try: 
	for port in range(1, 255):
		s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		socket.setdefaulttimeout(1)
		result = s.connect_ex((target, port))
		#print("Checking port {}".format(port))
		if result == 0:
			print("Port {} is open.".format(port))
		s.close()
except KeyboardInterrupt:
	print("\nExiting program")
	sys.exit()
except socket.gaierror:
	print("\nHostname could not be resolved.")
	sys.exit()
except socket.error:
	print("\nUnable to connect to the server.")
	sys.exit()
	
	
