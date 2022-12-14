import sys
import socket
from datetime import datetime

#================ Disclaimer Zotnierz ================
#Studies purpose only, any malicious activities are not tied to the code creator.
#================ ******************* ================

if len(sys.argv) == 2: # Define target IP
    target = socket.gethostbyname(sys.argv[1]) # Translate hostname to IPv4
else:
    print('Invalid amount of arguments.')
    print('Syntax: python scanner.py <ip>')

#Tool design
print("-" * 50)
print("Scanning target... " +target)
print("Time started: " +str(datetime.now()))
print("-" * 50)

try:
    for port in range(50,85): # Don't forget to specify the port range
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket.setdefaulttimeout(1)
        result = s.connect_ex((target, port)) # Returns an error indicator
        print("Checking port {}" .format(port)) # You can comment this line, to only print open ports
        if result == 0:
            print("Port {} is open" .format(port))
            s.close

except KeyboardInterrupt: # Ctrl + C
    print("\nExiting program...")
    sys.exit()

except socket.gaierror:
    print("Hostname could not be resolved.")
    sys.exit()

except socket.error:
    print("Couldn't connect to server.")
    sys.exit
