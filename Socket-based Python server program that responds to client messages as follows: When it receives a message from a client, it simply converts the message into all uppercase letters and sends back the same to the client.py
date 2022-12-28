#echo-server.py
import socket               # Import socket module

s = socket.socket()         # Create a socket object
host = socket.gethostname() # Get local machine name
port = 12345                # Reserve a port for your service.
s.bind((host, port))        # Bind to the port
print(f'Server started at {host}:{port}')
s.listen(5)                 # Now wait for client connection.
while True:
   c, addr = s.accept()     # Establish connection with client.
   print ('Got connection from', addr)
   req1 = c.recv(1024)
   req1 = str(req1,'utf-8')
   str1 = req1.upper()
   # print(str1)
   str1 = bytes(str1,'UTF-8')
   c.send(str1)
   c.close()                # Close the connection
    
    
# echo-client.py

import socket               # Import socket module
import os

s = socket.socket()         # Create a socket object
host = socket.gethostname() # Get local machine name
port = 12345                # Reserve a port for your service.

s.connect((host, port))
s.send(b"Sending request to UpperCase this line")
res1 = s.recv(1024)
print(res1)
s.close()                     # Close the socket when done
