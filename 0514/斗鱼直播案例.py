import unittest
from selenium import webdriver
from bs4 import BeautifulSoup
import lxml


class DouyuTest(unittest.TestCase):
    def setUp(self):
        print('setUp.....')
        # 创建浏览器
        self.driver = webdriver.Chrome()
        # 一条数据其实就是一个主播,点击下一页
        self.page_num = 1
        self.nums = 0

    def testTest(self):
        print('被测试的代码')
        self.driver.get("https://www.douyu.com/directory/all")
        while True:
            print("第几页",self.page_num)
            # prit(self.driver.page_source)
            soup = BeautifulSoup(self.driver.page_source, 'lxml')
            # 根据标签名和属性得到所有的主题名，
            h3_list = soup.find_all(name='h3', attrs={"class", "ellipsis"})
            # 观看人数
            num_list = soup.find_all(name='span', attrs={"class", "dy-num fr"})
            # for h3 in h3_list:
            #     #print(h3.get_text().strip())
            #     pass
            #
            # for num in num_list:
            #     print(num.get_text())
            title_name = zip(h3_list, num_list)
            for title, num in title_name:
                print('直播主题', title.get_text().strip(), "观看人数是", num.get_text().lstrip())
                self.nums += 1
            #点击下一页实现
            if self.driver.page_source.find('shark-pager-disable-next') != -1:
                #结束没有下一页
                break
            else:
                self.driver.find_element_by_class_name('shark-pager-next').click()

            self.page_num += 1

    def tearDown(self):
        print("测试的方法执行完毕后调用")
        print('直播页面共计:',self.page_num)
        print('主播人数',self.nums)
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()
