import sys
import pathlib

src_file=sys.argv[1]
dst_file=sys.argv[2]
'''
#creating source file
f=open(src_file,"w")
f.write("hello how are you")
'''

file=pathlib.Path(src_file)
if file.exists():
#opening source file
	f=open(src_file,"r")
	src_data=f.read()
	f.close()

#copying into destination file
	f1=open(dst_file,"w")
	f1.write(src_data)
	f1.close()
else:
	print ("File does not exist..!")
