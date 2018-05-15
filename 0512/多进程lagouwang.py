from queue import Queue
from lxml import etree
import requests
import json
from threading import Thread, Lock
import time

crawl_exit = False
parse_exit = False


# 创建采集数据的线程
class ThreadGet(Thread):

    def __init__(self, thread_name, page_queue, data_queue):
        super(ThreadGet, self).__init__()
        self.thread_name = thread_name
        self.page_queue = page_queue
        self.data_queue = data_queue
        self.headers = {"User-Agent": "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; WOW64; Trident/6.0)"}

    def run(self):
        while not crawl_exit:

            try:
                page = self.page_queue.get(block=False)
                url = "https://www.qiushibaike.com/8hr/page/" + str(page) + "/"
                print("%s采集线程开始工作了，页数是：%d" % (self.thread_name, page))
                request = requests.get(url, headers=self.headers)
                html = request.text
                # print(request.text)
                # 把数据装入队列
                time.sleep(1)
                self.data_queue.put(html)
            except Exception as e:
                pass
                break


# 创建解析数据的线程
class ThreadParse(Thread):

    def __init__(self, thread_name, data_queue, f, lock):
        super(ThreadParse, self).__init__()
        self.threadName = thread_name
        self.fileName = f
        self.data_queue = data_queue
        self.lock = lock

    def run(self):
        while not parse_exit:
            try:
                print("解析线程开始解析数据")
                html = self.data_queue.get(block=False)
                print("%s开始解析" % (self.threadName))
                self.parse(html)
                time.sleep(1)
            except Exception as a:
                pass
                print(a)
                # break

    # 解析数据
    def parse(self, html):
        content = etree.HTML(html)
        # xpath
        div_list = content.xpath("//div[contains(@id, 'qiushi_tag_')]")

        for di in div_list:
            item = {}
            user_image = di.xpath('.//div/a/img[@class="illustration"]/@src')
            user_name = di.xpath(".//div//h2/text()")
            text = di.xpath(".//a/div/span/text()")
            zan = di.xpath(".//div/span/i/text()")
            comments = di.xpath(".//div/span/a/i/text()")
            # print(user_name,user_image,text,zan,comments)
            if len(user_image) > 0:
                item["user_image"] = user_image[0]
            if len(user_name) > 0:
                item["user_name"] = user_name[0]
            if len(text) > 0:
                item["text"] = text[0]

            if len(zan) > 0:
                item["zan"] = zan[0]
            if len(comments) > 0:
                item["comments"] = comments[0]
            print(item)

            with self.lock:
                json.dump(item, self.fileName, ensure_ascii=False)


def main():
    global parse_exit
    global crawl_exit
    lock = Lock()
    # 定义装页数的队列，最多爬10页
    page_queue = Queue(10)
    for page in range(1, 11):
        page_queue.put(page)

    # 定义装每页数据的队列
    data_queue = Queue()

    # 创建三个采集线程用语：数据的采集（请求网络得到数据）
    # 存储三个采集线程
    thread_crawls = []
    thread_names = ['1', '2', '3']
    for thread_name in thread_names:
        crawl = ThreadGet(thread_name, page_queue, data_queue)
        # 启动
        crawl.start()
        thread_crawls.append(crawl)

    # 创建三个进程用语解析HTML页面的数据
    # 存储json数据
    f = open("丑事百科.json", 'a', encoding='utf-8')

    # with open("丑事百科.json",'a',encoding='utf-8') as f:
    # 存档文档
    thread_parses = []
    thread_names = ["j1", 'j2', 'j3']
    for thread_name1 in thread_names:
        parse = ThreadParse(thread_name1, data_queue, f, lock)
        parse.start()
        thread_parses.append(parse)

    # 等待采集线程接受主线程才能结束
    while not page_queue.empty():
        pass
    # 退出采集线程
    crawl_exit = True
    for crawls in thread_crawls:
        crawls.join()

    while not data_queue.empty():
        pass

    parse_exit = True

    for parse in thread_parses:
        parse.join()

    with lock:
        f.close()
    print('over')


if __name__ == '__main__':
    main()
