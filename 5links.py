import webbrowser,bs4,requests,time
from bs4 import BeautifulSoup

page=requests.get("https://www.google.co.in/search?ei=v0yaW4mnGMyGoASH4oTwDA&q=crazy&oq=crazy&gs_l=psy-ab.3..0i67k1j0l9.172836.174682.0.175331.7.6.0.0.0.0.244.872.2-4.4.0....0...1c.1.64.psy-ab..3.4.868...35i39k1j0i131k1j0i10k1.0.eqVjiLhuyUU")

print (page.status_code)
#print (page.content)

soup = BeautifulSoup(page.content, 'html.parser')

#print(soup.prettify())
'''
v=(soup.find_all(class_='r'))
f=(v[1].find('a')) 
print (f.text)
print (f.get('href'))
'''
b=0
#print (v[1].text)
while b<5:
	v=(soup.find_all(class_='r'))
	f=(v[b].find('a')) 
	print ("Headline of " + str(b+1) + " is:  " + f.text)
	print ("Link " + str(b+1) + " is:  "  + f.get('href'))
	print ("")
	b+=1

#x=(soup.find('a'))
#time.sleep(1)
#v=(x.find('a'))
#print (x.get('href'))

