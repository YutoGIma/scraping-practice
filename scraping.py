from selenium import webdriver
import chromedriver_binary
import time

driver = webdriver.Chrome(executable_path="C:\chromedriver.exe")

driver.get('https://www.google.co.jp/')
search_bar = driver.find_element_by_name("q")
search_bar.send_keys("沖縄")
search_bar.submit()

list = []

for tab in driver.find_elements_by_class_name('hdtb-mitem'):
    list.append(tab)

newsTab = list[2].find_element_by_xpath("a")
newsTab.click()

for news in driver.find_elements_by_class_name("mCBkyc"):
    print(news.text)

time.sleep(10)
print("finish")
driver.quit()