from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import re
from bs4 import BeautifulSoup

# 创建浏览器
# driver = webdriver.Chrome()

# 设置等待

# 请求淘宝
# SERVICE_ARGS = ['--load-images=false', '--disk-cache=false']

# driver = webdriver.Chrome(service_args=SERVICE_ARGS)
chrome_options = Options()
chrome_options.add_argument("--headless")
driver = webdriver.Chrome(chrome_options=chrome_options)

wait = WebDriverWait(driver, 10)
driver.get('https://www.taobao.com/')


def get_nums():
    # 等待搜索框
    wait.until(EC.presence_of_element_located((By.ID, 'q'))).send_keys('美食')
    # 获取点击搜索按钮
    driver.find_element_by_css_selector("#J_TSearchForm>div>button").click()
    # 获取所有页数
    num = driver.find_element_by_class_name('total').text
    page_num = re.compile(r"(\d+)")
    return page_num.search(num).group(1)


def get_pro_info():
    wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "#mainsrp-itemlist .items .item")))
    page_source = driver.page_source
    soup = BeautifulSoup(page_source, 'lxml')
    items = soup.select("#mainsrp-itemlist .items .item")
    # print(items)
    for i in items:
        item_dict = {}
        images = i.select('.J_ItemPic.img')[0].attrs['data-src']
        if not images:
            images = i.select('.J_ItemPic.img')[0].attrs['data-ks-lazyload']
        # 销售地
        location = i.select(".location")[0].text
        # 价格
        price = i.select(".price")[0].text
        # 商店名称
        name = i.select(".shopname")[0].text.strip()
        # 宝贝名称
        title = i.select('a[class="J_ClickStat"]')[0].text.strip()
        # 宝贝链接
        baby_link = i.select('a[class="J_ClickStat"]')[0].attrs['href']
        item_dict['图片链接'] = 'https:' + images
        item_dict['销售地'] = location
        item_dict['价格'] = price
        item_dict['商店名称'] = name
        item_dict['宝贝名称'] = title
        item_dict['宝贝链接'] = 'https:' + baby_link
        print(item_dict)
        with open('淘宝.txt', 'a', encoding='utf-8') as f:
            f.write(str(item_dict))


def next_page(page):
    print("=" * 50, page)
    try:
        # 判断页面是否加载成功
        input = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "#mainsrp-pager > div > div >div > div > input")))

        # 清空输入框
        input.clear()

        # 页面框添加页码
        input.send_keys(page)

        # 找到确定按钮点击确定
        driver.find_element_by_css_selector("#mainsrp-pager > div > div >div > div > span.btn.J_Submit").click()

        # 判断是否真正切换到对应的页面---- 判断是否高亮
        wait.until(EC.text_to_be_present_in_element((By.CSS_SELECTOR, "#mainsrp-pager > div > div > div > ul.items > li.item.active"), str(page)))
    except Exception as a:
        print(a)
        next_page(page)
    get_pro_info()


def main():
    get_num = get_nums()
    print('总页数', get_num)
    for page in range(1, int(get_num) + 1):
        next_page(page)
    driver.quit()


if __name__ == '__main__':
    main()
