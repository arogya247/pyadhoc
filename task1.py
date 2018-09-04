import datetime
import psutil,platform,webbrowser,os,sys
import uuid

now = datetime.datetime.now()

CPU=psutil.cpu_percent()
VM=psutil.virtual_memory()

x=input()
y=int(x)


if   y==2:
	print("CPU usage is:",CPU)
	print("RAM usage is:",VM)  
elif y==1:
	print ("The MAC address in formatted way is :",(hex(uuid.getnode()))) 
elif y==3:   
	print(platform.platform())
elif y==4:
	def is_connected():
		try:
        # connect to the host -- tells us if the host is actually
        # reachable
			socket.create_connection(("www.google.com", 80))
			return True
		except OSError:
			pass
			return False
elif y==6:
     	print (now)

