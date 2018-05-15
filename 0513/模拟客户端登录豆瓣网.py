from selenium import webdriver
import time

driver = webdriver.PhantomJS(executable_path='/usr/bin/phantomjs')
driver.get('https://www.douban.com')
time.sleep(1)
driver.save_screenshot('豆瓣首页.png')
# 输入账号
driver.find_element_by_id('form_email').send_keys('trayf521@126.com')
# 输入密码
driver.find_element_by_name('form_password').send_keys('afu123456')
# 保存验证码的图片
driver.save_screenshot('验证码.png')
# 输入验证码
check_code = input("验证码:")
driver.find_element_by_id('captcha_field').send_keys(check_code)
# 点击登录
driver.find_element_by_xpath('//input[@class="bn-submit"]').click()
# 休息一下
time.sleep(3)
driver.save_screenshot('首页.png')
# 保存登录信息
with open('首页.html', 'w', encoding='utf-8') as f:
    f.write(driver.page_source)

driver.quit()
