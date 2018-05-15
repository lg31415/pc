from selenium import webdriver

drive = webdriver.PhantomJS(executable_path="/usr/bin/phantomjs")

drive.get("http://www.baidu.com")

print(drive.title)

drive.save_screenshot('baidu.png')
drive.quit()
