from urllib.request import urlopen,Request


headers = {
"Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
#"Accept-Encoding":"gzip, deflate, br",
"Accept-Language":"zh,zh-CN;q=0.9,en;q=0.8,zh-HK;q=0.7,zh-TW;q=0.6",
"Cache-Control":"max-age=0",
"Connection":"keep-alive",
"Cookie":"_uab_collina=152569746045365080413077; htVD_2132_saltkey=kPcTTekJ; htVD_2132_lastvisit=1525734877; htVD_2132_client_created=1525744027; htVD_2132_client_token=148709B53CB83C532EA6CE47090E4927; htVD_2132_auth=881cppQoOk%2B017GGYSNhlsSrzpAaYftlaZt77Lj8Ov4F7e4QDuLthKQCkJm3onh1UfBIO8DP4atftfK9nEVhS9CSqLg; htVD_2132_connect_login=1; htVD_2132_connect_is_bind=1; htVD_2132_connect_uin=148709B53CB83C532EA6CE47090E4927; htVD_2132_nofavfid=1; htVD_2132_smile=1D1; htVD_2132_pc_size_c=0; htVD_2132_connect_last_report_time=2018-05-09; htVD_2132_ttask=360104%7C20180509; htVD_2132_visitedfid=2D16D24D4D5; htVD_2132_ulastactivity=1525849022%7C0; htVD_2132_lastact=1525849022%09home.php%09spacecp; htVD_2132_lastcheckfeed=360104%7C1525849022; Hm_lvt_46d556462595ed05e05f009cdafff31a=1525697461,1525749737,1525826462,1525849028; Hm_lpvt_46d556462595ed05e05f009cdafff31a=1525849028",
"Host":"www.52pojie.cn",
"Referer":"https://www.baidu.com/link?url=RjBgzkaqt1LVgwpvtT_iCRYCJDLBD33ia3y_eCE9QPkZueh7Egt0jX_FpolzKZMz&wd=&eqid=80d1e57d00003797000000035af29bc0",
"Upgrade-Insecure-Requests":"1",
"User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.139 Safari/537.36",
    }

request = Request('https://www.52pojie.cn/home.php?mod=space&uid=360104',headers=headers)
response = urlopen(request)
#print(response.read().decode("GB18030"))
#print(html.text)
with open('1.html','w') as f:
    f.write(response.read().decode("GB18030"))