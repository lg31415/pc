from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys

def main():

    driver = webdriver.Chrome()
    driver.get("https://www.baidu.com")
    driver.find_element_by_id('kw').send_keys('尚硅谷')
    driver.find_element_by_id('su').click()
    time.sleep(2)
    driver.save_screenshot('尚硅谷.png')
    #全选ctrl+a
    data = driver.find_element_by_id('kw').send_keys(Keys.CONTROL,'a')
    print(data)
    data1 = driver.find_element_by_id('kw').send_keys(Keys.CONTROL,'x')
    print(data1)

    driver.quit()

if __name__ == '__main__':
    main()