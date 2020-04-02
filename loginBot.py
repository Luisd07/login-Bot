# Bot to login to website

from selenium import webdriver
import os

# usename and password stored in enviornment variable
usernameStr = os.environ.get('botUser')
passwordStr = os.environ.get('botPass')

# tells selenium we are using chrome
browser = webdriver.Chrome()

# the website we are trying to log into
browser.get(("https://auth.dadeschools.net/_auth/dsLogon.aspx?ru=aHR0cDovL21kY3BzcG9ydGFsLmRhZGVzY2hvb2xzLm5ldC8="))

# finding the login box on the website and entering our usename
username = browser.find_element_by_id('txtUsername')
username.send_keys(usernameStr)

# finding the password box and entering in our pasword
password = browser.find_element_by_id('txtPassword')
password.send_keys(passwordStr)

# clicks the sign in button.
signInButton = browser.find_element_by_id('btnLogon')
signInButton.click()
