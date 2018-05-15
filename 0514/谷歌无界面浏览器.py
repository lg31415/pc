from selenium import webdriver
from selenium.webdriver.chrome.webdriver import Options

# driver = webdriver.PhantomJS('/usr/bin/phatomjs')
chrome_options = Options()
# 添加无头
chrome_options.add_argument('--headless')
driver = webdriver.Chrome(chrome_options=chrome_options)
driver.get('https://www.google.com/')
driver.save_screenshot('谷歌.png')
print(driver.title)
driver.quit()