import sys,time

user_input=sys.argv[1:]

product=1
for i in user_input:
	product=product*int(i)
	print (product)
	time.sleep(1)
