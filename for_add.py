import sys,time

user_input=sys.argv[1:]
sum=0

for i in user_input:
	sum=sum+int(i)
	print(sum)
