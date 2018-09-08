
import socket
#we are looking for UDP(user data protocol)
#        ip_version4,UDP
s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
#defining ip and port below
ip="127.0.0.1"
port=7890

#binding ip and port function with bind function which takes input as tuple
s.bind((ip,port))


#receiving data from target machine
while 4>2:
	x=s.recvfrom(100)
	print("Message is:",x[0])
s.close()

