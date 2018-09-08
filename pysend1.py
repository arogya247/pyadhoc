
import  socket
#  we are looking for UDP (user datagram protocol )
#              ip_version4,         UDP 
s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
# defining ip and port below 
ip="127.0.0.1"
port=7890

while  4 > 2 :
#  sending  data to  target machine 
	msg=input("enter your message :   ")
	msg=msg.encode()
	s.sendto(msg,(ip,port))


