import socket,commands

s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

ip="127.0.0.1"
port1=7890
port2=8888

s.bind(("",port2))

user=s.recvfrom(20)
password=s.recvfrom(20)
print (user[0])
print (password[0])

if ("root") in user and ("123") in password:
	msg1=("Correct")
	s.sendto(msg1,(ip,port1))
	print ("OK")
	while True:
		data=s.recvfrom(20)
		recv_cmd=data[0]
		d=commands.getoutput(recv_cmd)
		print (d)
else:
	msg=("wrong")
	s.sendto(msg,(ip,port1))
	print ("INVALID PASSWORD OR USERNAME..!!")
	exit()
	
		
	

	

	
