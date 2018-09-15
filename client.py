import socket,commands

s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

ip="127.0.0.1"
port1=7890
port2=8888

s.bind(("",port1))

user=raw_input("Enter Username:  ")
password=raw_input("Enter Password:  ")
s.sendto(user,(ip,port2))
s.sendto(password,(ip,port2))

received=s.recvfrom(20)
if ("wrong") in received[0]:
	print ("invalid")
	exit()
elif ("Correct") in received[0]:
	while True:
		cmd=raw_input("Enter Command:  ")
		a=commands.getoutput(cmd)
		if "not found" in a:
			print ("Invalid Command")
			continue
		s.sendto(cmd,(ip,port2))
	

	
