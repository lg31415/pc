import re
import os
import requests

def tests_save(tests,tests_name):
    if not os.path.exists('./test2/'):
        os.makedirs('./test2/')
    print('正在下载文档：' + tests_name + '........')
    num = 1
    with open('./test2/'+tests_name,'w') as f :
        for t in tests:
            f.write(t)
            if num == 1:
                f.write(' '*100)
                num += 1
    print('文档' + tests_name + '下载完毕！')

def img_save(img_name,img_link):
    response = requests.get(img_link)
    if not os.path.exists('./img2/'):
        os.makedirs('./img2/')
    print('正在下载图片：'+img_name+'........')
    with open('./img2/'+img_name,'wb') as f :
        for co in response.iter_content(1024):
            if not co :
                break
            f.write(co)
    print('图片' + img_name + '下载完毕！')

def select_img_test(part):
    pattern = re.compile(r'src="(.*?)"')
    p = pattern.search(part).group(1)

    img_name = p[p.find('/')+1:]
    img_link = 'http://www.atguigu.com/' + p
    img_save(img_name,img_link)

    pattern = re.compile(r'[\u4e00-\u9fa5]+')
    tests = pattern.findall(part)
    tests_name = p[p.find('/')+1:p.rfind('.')] + '.txt'
    tests_save(tests,tests_name)


def select_part(content):

    pattern1 = re.compile(r'<div class="teacher_content" style="border-top:none;">(.*?)<a name="lhf"', re.S)
    part1 = pattern1.search(content).group()
    select_img_test(part1)

    pattern2 = re.compile(r'<div class="teacher_content"( )?>(.*?)<span class="teacherfont">',re.S)
    part2s = pattern2.findall(content)
    for par in part2s:
        select_img_test(par[1])


    pattern3s = re.compile(r'<div class="teacher_content">[\r\n]+[ ]+<img src="pics/lyteacher.jpg"(.*?)<!--左侧结束-->', re.S)
    parts3s = pattern3s.search(content).group()
    pattern3 = re.compile(r'<div class="teacher_content">.*?</div>',re.S)
    part3s = pattern3.findall(parts3s)
    for part3 in part3s:
        select_img_test(part3)


def main():
    url = 'http://www.atguigu.com/teacher.shtml'
    response = requests.get(url)
    content = response.content.decode()
    select_part(content)

if __name__ == '__main__':
    main()