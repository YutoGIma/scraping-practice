from selenium import webdriver
import chromedriver_binary
import time
import config

driver = webdriver.Chrome(executable_path="C:\chromedriver.exe")

account = config.account
password = config.password
text ="seleniumでログインしてツイートしています。"
print(account)
driver.get('https://twitter.com/login/')
time.sleep(3)
loginUser = driver.find_element_by_name("text")
loginUser.send_keys(account)
time.sleep(3)
nextButton = driver.find_elements_by_class_name("r-usiww2")
nextButton[2].click()
time.sleep(3)
loginPassword = driver.find_element_by_name("password")
loginPassword.send_keys(password)
time.sleep(3)
loginButton = driver.find_elements_by_class_name("r-sdzlij")
loginButton[2].click()
time.sleep(3)
tweetText = driver.find_element_by_class_name("notranslate")
tweetText.click()
tweetText.send_keys(text)
time.sleep(1)
tweetButton = driver.find_elements_by_class_name("r-19u6a5r")
tweetButton[0].click()

time.sleep(10)
print("finish")
driver.quit()