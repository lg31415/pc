from selenium import webdriver
import time
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get('http://www.neihan8.com/article/list_5_1.html')
time.sleep(1)
# data = driver.find_element_by_id('login')
data = driver.find_element(By.ID,value='login')
print(data.text)
driver.quit()