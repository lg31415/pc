from selenium import webdriver
from selenium.webdriver.common.by import By

# 创建浏览器
driver = webdriver.Chrome()


def main():
    driver.get("https://www.bilibili.com/")
    # print(driver.page_source)
    # driver.find_element_by_class_name('login-btn').click()
    driver.find_element(By.CLASS_NAME, 'login-btn').click()
    # QQ登录
    # driver.find_element(By.CLASS_NAME, "btn qq").click()
    # driver.find_element(By.ID, "login-username").send_keys('1154718748@qq.com')
    # driver.find_element(By.ID, "login-passwd").send_keys("zx2666612")
    print(driver.page_source)
    driver.quit()


if __name__ == '__main__':
    main()
