
from selenium import webdriver 
from time import sleep 
  
usr=input('Enter Email Id:')  
pwd=input('Enter Password:')  
  
driver = webdriver.Chrome() 
driver.get('https://www.github.com/login') 
print ("Opened Github ") 
sleep(1) 
  
username_box = driver.find_element_by_id('login_field') 
username_box.send_keys(usr) 
print ("Email Id entered") 
sleep(1) 
  
password_box = driver.find_element_by_id('password') 
password_box.send_keys(pwd) 
print ("Password entered") 
  
login_box = driver.find_element_by_class_name('btn btn-primary btn-block') 
login_box.click() 
  
print ("Done") 
input('Press anything to quit') 
driver.quit() 
print("Finished")
