import matplotlib.pyplot as plt
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
v=s.recvfrom(100)
a=v[0]
print("Message is:",a)


# Python program to count the number of occurrence  
def word_count(str):
    counts = dict()
    words = str.split()

    for word in words:
        if word in counts:
            counts[word] += 1
        else:
            counts[word] = 1

    return counts

print( word_count(a))



#plotting graph out of dict
#use ticks as x list is of string type

xticks=list(word_count(a).keys())
print (xticks)

y=list(word_count(a).values())
print (y)

x=range(len(xticks))

#ticks used
plt.xticks(x,xticks)
#labelling
plt.xlabel("Name of Word")
plt.ylabel("Word Count")

plt.title("My First Graph")
plt.scatter(x,y)
plt.plot(x,y)
plt.show()

