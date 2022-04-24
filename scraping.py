from selenium import webdriver
import chromedriver_binary
import time

driver = webdriver.Chrome(executable_path="C:\chromedriver.exe")

driver.get('https://www.google.co.jp/')
search_bar = driver.find_element_by_name("q")
search_bar.send_keys("python")
search_bar.submit()

time.sleep(10)
print("finish")
driver.quit()