#Python Strings to Bytes
import socket

while True:
 data = mysock.recv(512)
 if ( len(data) < 1 ) :
  break
 mystring = data.decode()
print(mystring)
