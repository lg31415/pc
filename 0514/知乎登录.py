from selenium import webdriver
import time
import base64
from PIL import Image
from pytesseract import image_to_string

driver = webdriver.Chrome()


def get_cap():
    try:
        image = Image.open("cap.jpg")
        # 识别
        text = image_to_string(image)
        print("识别的验证码是", text)
        cmd = input("是否手动输入验证码Y，不输入N:")
        if cmd == 'Y':
            text = input("输入验证吗：")
            return text
        elif cmd == 'N':
            return text
    except Exception as a:
        print("验证失败")
        text = input("请手动输入验证码:")
        return text


def save_image(image_data):
    # base64
    image = image_data[len("data:image/jpg;base64,"):].replace('&#10;', '').replace("%0A", '')

    data_image = base64.b64decode(image)
    with open('cap.jpg', 'wb') as f:
        f.write(data_image)


def main():
    driver.get('https://www.zhihu.com/signup?next=%2F')
    time.sleep(2)
    # 找到登录按钮
    driver.find_element_by_xpath('//div[@class="SignContainer-switch"]/span').click()
    time.sleep(1)
    # 账号
    driver.find_element_by_name("username").send_keys('trygf521@126.com')
    driver.find_element_by_name("password").send_keys('afu123456')
    driver.save_screenshot('输入账号密码.png')

    if driver.page_source.find('Captcha-englishContainer') != -1:
        print('英文')
        image = driver.find_element_by_xpath('//div[@class="Captcha-englishContainer"]/img')
        image_data = image.get_attribute("src")
        if len(image_data) > len("data:image/jpg;base64,"):
            # 保存
            save_image(image_data)
            # 失败重新加载
            cap = get_cap()
            print("得到的验证码是", cap)
            driver.find_element_by_name("captcha").send_keys(cap)
    elif driver.page_source.find('Captcha-chineseContainer') != -1:
        print("中文验证")
        image = driver.find_element_by_xpath('//div[@class="Captcha-chineseContainer"]/img')
        image_data = image.get_attribute('src')
        if len(image_data) > len('data:image/jpg;base64,'):
            # 保存
            save_image(image_data)
            # 失败重新加载
            cap = get_cap()
            print('得到的验证码是', cap)
            driver.find_element_by_name('captcha').send_keys(cap)
    # 点击登录
    driver.find_element_by_xpath('//div[@class="Login-content"]/form/button').click()
    time.sleep(2)
    driver.save_screenshot('登录成功.png')
    driver.quit()


if __name__ == '__main__':
    main()
