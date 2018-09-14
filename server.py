import socket,commands

s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

#ip="127.0.0.1"
port=7890

s.bind(("",port))
while True:
	
	data=s.recvfrom(20)
	recv_cmd=data[0]
	print (recv_cmd)


	
