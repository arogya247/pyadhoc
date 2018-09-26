from selenium import webdriver

driver=webdriver.Chrome()
driver.get("https://web.whatsapp.com")

name=input("Enter the name of user to send the message: ")
msg=input("Emter your message: ")
count=int(input("Enter number of times you want to end the message: "))




user = driver.find_element_by_xpath('//span[@title="%s"]'%name)
user.click()

msg_box=driver.find_element_by_class_name("_2S1VP")

for i in range(count):
	msg_box.send_keys(msg)
	button=driver.find_element_by_class_name("_35EW6")
	button.click()

