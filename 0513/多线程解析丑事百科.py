from queue import Queue
from threading import Thread, Lock
import requests
import time
from lxml import etree
import json

collect_a = False
resolver_b = False
lock = Lock()


# 创建采集进程
class ThreadGet(Thread):
    def __init__(self, data_queue, get, page_queue):
        super(ThreadGet, self).__init__()
        self.data_queue = data_queue
        self.get = get
        self.page_queue = page_queue
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.139 Safari/537.36'}

    def run(self):
        while not collect_a:
            try:
                print('采集进程开始工作了')
                page = self.page_queue.get(block=False)
                url = "https://www.qiushibaike.com/8hr/page/" + str(page) + "/"
                request = requests.get(url, headers=self.headers)
                html = request.text
                time.sleep(1)
                self.data_queue.put(html)
            except Exception as s:
                print(s)
                pass
                break


# 创建解析进程
class ThreadParse(Thread):
    def __init__(self, parse1, data_queue, f, lock):
        super(ThreadParse, self).__init__()
        self.parse1 = parse1
        self.data_queue = data_queue
        self.f = f
        self.lock = lock

    def run(self):
        while not resolver_b:
            try:
                print("开始解析")
                html = self.data_queue.get(block=False)
                self.parse(html)
                time.sleep(1)
            except Exception as e:
                pass

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
                json.dump(item, self.f, ensure_ascii=False)


def main():
    global collect_a
    global resolver_b

    # 创建最页面队列最多可解析shiye
    page_queue = Queue(10)
    for page in range(1, 11):
        page_queue.put(page)

    # 创建采集进程实例
    # 数据存放队列
    data_queue = Queue()

    get_queue = []

    gets_queue = ['1', '2', '3']
    for get in gets_queue:
        datas = ThreadGet(data_queue, get, page_queue)
        datas.start()
        get_queue.append(datas)

    # 创建解析进程
    f = open('丑事百科.json', 'a', encoding='utf-8')
    parse_queue = []
    parses_queue = ['1', '2', '3']
    for parse1 in parses_queue:
        data = ThreadParse(parse1, data_queue, f, lock)
        data.start()
        parse_queue.append(data)

    # 判断页面是否还有没有就退出进程
    while not page_queue.empty():
        pass
    collect_a = True
    for a in get_queue:
        a.join()

    # 判断还有没有数据没有就退出
    while not data_queue.empty():
        pass
    resolver_b=True
    for b in parse_queue:
        b.join()

    while lock:
        f.close()

    print('over')


if __name__ == '__main__':
    main()
