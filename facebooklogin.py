from selenium import webdriver
from getpass import getpass
from webdriver_manager.chrome import ChromeDriverManager

username=input('P1 Enter Your Facebook username,email or phone no.: ')
passwd=getpass('Enter Your Facebook Password: ')

#driver=webdriver.Chrome(ChromeDriverManager().install)
driver=webdriver.Chrome(executable_path='C:/chromedriver')

driver.get('https://www.facebook.com')

txtUsername=driver.find_element_by_id('email')
txtUsername.send_keys(username)

txtpasswd=driver.find_element_by_id('pass')
txtpasswd.send_keys(passwd)

btnLogin=driver.find_element_by_id('u_0_b')
btnLogin.submit()