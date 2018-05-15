import requests
from lxml import etree
import os


header = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.139 Safari/537.36'}
'''
"".join(列表):列表转换为字符串
str.rfind("/"):查找某一个符号的位置
list.index(str):查找列表中str的下标
str.replace("xxx"):数据清洗

'''

# 写入
def write_msg(name, message, img):
    request = requests.get(img)
    if not os.path.exists('./image/'):
        os.mkdir('./image/')
    with open("./image/" + name[0] + ".jpg", 'wb') as f:
        f.write(request.content)
    if not os.path.exists('./text/'):
        os.makedirs('./text/')
    with open("./text/" + name[0] + "信息.txt", 'w') as f:
        f.write(message)

#动态写入所有信息
def write_all(all_image, name_list):
    for i in all_image:
        all_images = "http://www.atguigu.com/" + i
        # print(all_image)
        requestt = requests.get(all_images)
        names = all_images[all_images.rfind('/') + 1:-4]
        with open("./image/" + names + ".jpg", 'wb') as f:
            f.write(requestt.content)
        with open('./text/' + names + '.txt', 'w') as f:
            f.write(name_list[all_image.index(i)])

#主函数
def main():
    request = requests.get("http://www.atguigu.com/teacher.shtml")
    html = request.content
    sg_index = etree.HTML(html)
    message = sg_index.xpath('//div[@class="teacher_tong_l"]/text()')
    img = sg_index.xpath('//div[@class="teacher_tong_l"]/img/@src')
    all_image = sg_index.xpath('//div[@class="teacher_content"]/img/@src')
    img = "http://www.atguigu.com/" + img[0]
    # 列表转换成字符串
    message = ''.join(message)
    message = message.replace('\r\n', '').replace('\u3000', '')
    #新建空列表准备存放所有的信息
    name_list = []
    for num in range(1, len(all_image) + 1):
        all_mes = sg_index.xpath('//div[@class="teacher_content"]' + '[' + str(num) + ']' + '//text()')
        # print(all_mes)
        all_mes = ''.join(all_mes)
        name_list.append(all_mes)
    write_all(all_image, name_list)


if __name__ == '__main__':
    main()
