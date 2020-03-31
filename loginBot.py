from selenium import webdriver


usernameStr = "0400990"
passwordStr = "luism123"

browser = webdriver.Chrome()

browser.get(("https://auth.dadeschools.net/_auth/dsLogon.aspx?ru=aHR0cDovL21kY3BzcG9ydGFsLmRhZGVzY2hvb2xzLm5ldC8="))

username = browser.find_element_by_id('txtUsername')
username.send_keys(usernameStr)

password = browser.find_element_by_id('txtPassword')
password.send_keys(passwordStr)

signInButton = browser.find_element_by_id('btnLogon')
signInButton.click()
