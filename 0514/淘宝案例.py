from selenium import webdriver
from selenium.webdriver.support.ui import  WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import re
#创建浏览器
driver = webdriver.Chrome()
#等待多长时间
wait = WebDriverWait(driver,5)

driver.get('https://www.taobao.com/')


def get_nums():

    # 登录等待搜索框出现我们的指定的元素已经加载好了
    input = wait.until(EC.presence_of_element_located((By.ID,"q")))
    input.send_keys('美食')
    # 得到索索按钮点击搜索确定
    driver.find_element_by_css_selector("#J_TSearchForm>div>button").click()

    # 得到多少页

    text = driver.find_element_by_class_name('total').text
    page_num = re.compile(r"(\d+)").search(text).group(1)

    return page_num

def main():

    # 第一部分得到我们的美食所有页，
    get_num = get_nums()

    print('美食总页数',get_num)
    driver.quit()

if __name__ == '__main__':
    main()