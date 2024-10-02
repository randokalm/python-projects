from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

usernameStr = 'erdalaskin716@gmail.com'
passwordStr = 'cimpyp-jincyc-5guxsA'

# Initialize the browser
browser = webdriver.Chrome()
browser.get('https://accounts.google.com/ServiceLogin?service=mail&continue=https://mail.google.com/mail/#identifier')

# Fill in the username and click the "Next" button
username = WebDriverWait(browser, 10).until(
    EC.presence_of_element_located((By.ID, 'identifierId'))
)
username.send_keys(usernameStr)

nextButton = browser.find_element(By.ID, 'identifierNext')
nextButton.click()

# Wait for the transition to the password field
password = WebDriverWait(browser, 10).until(
    EC.presence_of_element_located((By.NAME, 'password'))
)
password.send_keys(passwordStr)

signInButton = browser.find_element(By.ID, 'passwordNext')
signInButton.click()
