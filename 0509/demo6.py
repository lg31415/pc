import requests
import re
import os


def write_img(all_imgs):
    for img in all_imgs:
        url = "http://www.atguigu.com/" + str(img) + '.jpg'
        print(url)
        request = requests.get(url)

        # 判断images文件夹是否存在不存在就创建然后写入数据
        if not os.path.exists("./images/"):
            os.makedirs("./images/")
        with open("./images/" + url[url.rfind('/'):-4] + '.jpg', 'wb') as f:
            f.write(request.content)

        # 信息写入texts文件夹内使用os模块判断是否存在文件夹不存在就创建
        # 因为不能吧all_party的列表下标写死，所以就根据所有图片的for循环都是从0开始
        # 动态写入每个人的信息
        if not os.path.exists('./texts/'):
            os.makedirs('./texts/')
        with open("./texts/" + url[url.rfind('/'):-4] + '.txt', 'w') as f:
            f.write(all_party[all_imgs.index(img)])


all_party = []  # 存放所有人的信息
all_imgs = []  # 存放所有人的照片链接


def main():
    request = requests.get("http://www.atguigu.com/teacher.shtml")
    html = request.content.decode()
    content2 = re.compile(r'<div class="teacher_content"(.*?)<p style="padding-top:10px;">', re.S)
    con2 = content2.findall(html)
    # 特殊字符第一位
    hsp = re.compile(r'<div class="teacher_content"(.*?)<a name="lhf">', re.S)
    hsp = hsp.findall(html)
    hsp = str(hsp)
    hsp = hsp.split('l">')[1]
    #数据过滤
    hsp = str(hsp).replace("</div>", '').replace('<div class="r">', '') \
        .replace("']", '').replace("\\r",'').replace("\\n",'').replace("\\u3000",'')
    # 加进空列表
    all_party.append(hsp)
    content = re.compile(r'(.*?)<img src="(.*?).jpg">')
    all_str = content.findall(str(con2))
    for s in all_str[2:]:
        s = str(s)
        # 数据过滤
        s = s.replace('<div class="weibo">', '').replace('<div class="l">', '') \
            .replace('</div>', '').replace('<div class="r">', '').replace('<p>', '').replace('</p>', '') \
            .replace('<br />', '').replace("<br>", '').replace('<br/>', '').replace('<span class="teacherfont">', '') \
            .replace('<a href="download.shtml#1">', '').replace('</a>', '').replace('</span>', '').replace('<span class="teachervideo" >', '') \
            .replace('<a name="zxf">', '').replace('<div class="teacher_content">', '').replace("('", '').replace('("', '').replace("\\\\r",'')\
            .replace("\\\\n",'').replace("\\\\u3000",'').replace("',",'').replace("'>",'').replace('"','')
        s = s[:s.rfind(',')]
        all_party.append(s)

    # 特殊字符最后一位r
    sls = re.compile(r'<img src="teacher/xnw.jpg"(.*?)<p style="padding-top:10px;">', re.S)
    sls = sls.findall(html)
    #数据过滤
    sls = str(sls).replace("'>", '').replace('<p>', '').replace('</p>', '').replace("']", '').replace("\\r",'').replace("\\n",'').replace("\\u3000",'').replace("'[", '')
    all_party.append(str(sls))

    # 全部照片
    img = re.compile(r'<img src="(.*?).jpg">')
    all_img = img.findall(str(con2))
    for i in all_img:
        i = i.split('="')[-1:]
        i = str(i).split("['")[1]
        i = str(i).split("']")[0]
        all_imgs.append(i)
    # 调用函数
    write_img(all_imgs)


if __name__ == '__main__':
    main()
