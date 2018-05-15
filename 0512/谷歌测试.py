from selenium import webdriver
import time

drive = webdriver.Chrome()

drive.get("https://www.baidu.com")

print(drive.title)

drive.save_screenshot('baidu.png')

drive.find_element_by_id('kw').send_keys('谁会送我茶杯')
drive.find_element_by_id('su').click()
time.sleep(2)
drive.save_screenshot('谁？.png')

drive.quit()