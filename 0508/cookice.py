from urllib.request import Request,urlopen

def main():

    un_hander= {
        "Accept": " text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
        "Accept-Language": " zh,zh-CN;q=0.9,en;q=0.8,zh-HK;q=0.7,zh-TW;q=0.6",
        "Cache-Control": " max-age=0",
        "Connection": " keep-alive",
        "Cookie": " _uab_collina=152569746045365080413077; htVD_2132_pc_size_c=0; htVD_2132_saltkey=kPcTTekJ; htVD_2132_lastvisit=1525734877; htVD_2132_con_request_uri=https%3A%2F%2Fwww.52pojie.cn%2Fconnect.php%3Fmod%3Dlogin%26op%3Dcallback%26referer%3Dforum.php%253Fmod%253Dforumdisplay%252526fid%253D62%252526filter%253Ddigest%252526digest%253D1; htVD_2132_client_created=1525744027; htVD_2132_client_token=148709B53CB83C532EA6CE47090E4927; htVD_2132_auth=881cppQoOk%2B017GGYSNhlsSrzpAaYftlaZt77Lj8Ov4F7e4QDuLthKQCkJm3onh1UfBIO8DP4atftfK9nEVhS9CSqLg; htVD_2132_connect_login=1; htVD_2132_connect_is_bind=1; htVD_2132_connect_uin=148709B53CB83C532EA6CE47090E4927; htVD_2132_stats_qc_login=3; htVD_2132_ttask=360104%7C20180508; htVD_2132_nofavfid=1; htVD_2132_connect_last_report_time=2018-05-08; htVD_2132_smile=1D1; htVD_2132_st_p=360104%7C1525744091%7Ca8b6f19e60693efe374c240bd6d30260; htVD_2132_visitedfid=16D2D5D74D77; htVD_2132_viewid=tid_734813; htVD_2132_ulastactivity=1525749722%7C0; htVD_2132_lastcheckfeed=360104%7C1525749723; Hm_lvt_46d556462595ed05e05f009cdafff31a=1525697461,1525749737; htVD_2132_lastact=1525749725%09home.php%09space; Hm_lpvt_46d556462595ed05e05f009cdafff31a=1525749738",
        "Host": " www.52pojie.cn",
        "Upgrade-Insecure-Requests": " 1",
        "User-Agent": " Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.139 Safari/537.3",

    }
    url = 'https://www.52pojie.cn/home.php?mod=space&uid=360102'
    request = Request(url)

    response = urlopen(request)
    print(response.read().decode('GBK'))

if __name__ == '__main__':
    main()