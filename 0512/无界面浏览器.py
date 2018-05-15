from selenium import webdriver

driver = webdriver.PhantomJS(executable_path='/usr/bin/phantomJS')

driver.get("http://www.baidu.com")

print(driver.title)

print(driver.page_source)
driver.save_screenshot('baidu.png')

driver.quit()