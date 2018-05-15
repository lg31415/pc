from selenium import webdriver
import time

# 创建浏览器
driver = webdriver.Chrome()

driver.get('https://www.baidu.com/')

driver.find_element_by_id('kw').send_keys('尚硅谷')
driver.find_element_by_id('su').click()
time.sleep(4)
driver.save_screenshot('硅谷.png') 
with open('硅谷.html', 'w', encoding='utf-8') as f:
    f.write(driver.page_source)
driver.quit()
