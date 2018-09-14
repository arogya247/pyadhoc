import socket,commands

s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

ip="127.0.0.1"
port=7890

while True:
	cmd=raw_input()
	s.sendto(cmd,(ip,port))
	
