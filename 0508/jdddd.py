from urllib.request import Request,urlopen
import requests

# def main():
#     un_hender = {
#         "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
#         "Accept-Language": "zh,zh-CN;q=0.9,en;q=0.8,zh-HK;q=0.7,zh-TW;q=0.6",
#         "Cache-Control": "max-age=0",
#         "Connection": "keep-alive",
#         "Cookie": "__jdu=1977135510; PCSYCityID=1; unpl=V2_ZzNtbRdTERQmX0NQcx9aDGJTRV9KUEASIgATBnMeCFJuBRFZclRCFXwUR1BnGFUUZwsZXEVcQBVFCHZXchBYAWcCGllyBBNNIEwHDCRSBUE3XHxcFVUWF3RaTwEoSVoAYwtBDkZUFBYhW0IAKElVVTUFR21yVEMldQl2VHMfWgVlBxZdQ2dzEkU4dlR4GVoNbzMTbUNnAUEpDUJceRFYSGcLFFtCVUcRdQl2VUsa; CCC_SE=ADC_xvgjOAgT%2fpXeR%2bWMyHxk%2fgHlIIaAxLAdVq8QA3kT7p%2fmMMRqBU%2fQ71sU6khge2lKs095aR%2bIWJHPb%2bLzMsR41tWN%2f2ff68VgYIUII6%2b1JUnkkI%2bt0J%2bi0B0bdDPMFYAeJxy0SdNe2A2CD%2bv8ik0WOpqfFqBaIkA%2fkQ2zY4gMHCfq7%2bKR%2beYB0vRxUNnJLdriwc76d1ooZw2OJzWDkJMPFxlO5wEjZoCyTcszEAiq%2b9Qn78O2e%2fy1cdAuxa2zrHL7blJqR0djL%2fIqPNvqoXgZF3xogsv1GC8phEpJ800uI%2fNOb6NPtLjWNfWHj5TaG%2fZC0jfolXyo4LKWexDDmd3jTVO6Sb4SzYhGD%2bGXeZ%2fBcMugaMae80nVlP0qF10BO37ARZ5jsCw5r%2fqw%2bIAsk5GT6lRY%2fJ5%2bMshZwm2hG7xOT%2fahDlbY6x%2faoeKskaBrJ595hys9hicckqOPflME3Zm9nBu88%2faf5C1eIEj5BCk4Ia2URVFa43DX5ZlFOCtj4kZUAKDGbInHg35CTUJ8McIDddQIpDrvGkEnMLVyQAgocDTtZUBo3sjiDDcaEgjJnJf4; __jda=122270672.1977135510.1525749724.1525749725.1525777593.2; __jdc=122270672; shshshfpa=d87a5592-c3b9-dc19-f153-95f78c52021a-1525777595; shshshfpb=095858767daf647b15660045411c69ad1a490e57cfbc697f95af184b5e; cid=NWJFMzUwNnlKMzU0N2pYNjk4OHZPMDcyMXBPMzMwMnVDNjc0M2lRMjE2NGdPNTM4; _jrda=1; _jrdb=1525777605046; 3AB9D23F7A4B3C9B=ZVK5XTXGGQMTEPBDC4ZD3TTM2IXFIGYBJIH2HCKHANV2XOZGJ72TREQAFWCKKAOIGTI7H3VACCKWOTEUHRLO5ON2SU; wlfstk_smdl=gz44fm0s1n5n2xzem0as0r48kpq5let1; TrackID=1LB5tEWkI0YBgNjdNqQpaeS4EmGMw8hACL-RW1ihbKEI4gRH2d5KA67eR-JPwMc6yY7okt-KSRzjYEcf9o0npBs9GPbv119MEt3PVedyd--RGgYZMJKdig2XXBTwKhp7V; pinId=TYeoPsPRbF4R-DoDjWKMVQ; pin=15853129020_p; unick=WitheK; thor=5F9F41A19B6F78B9E414FE39AFFF94523C4607D4EB5FCE0227D7C2E44744258B7A5F8294F2D5AF678B4D6C948FB1BD2031E0FBD93FA12FC381932DE4BF9C48D42CCAA2FD2B6961705064BE4A9118746DA7A7A7E6E0269B929CC3C057AF328EDE19A306C22625E0F13DF957EEF7DB872DD366ABA315730BD39CE3542D808AFA468C22F3A02B7505348117BE703371E6D7; _tp=zsVAGnJ5E6TLA%2Bmfte%2FKyA%3D%3D; _pst=15853129020_p; ceshi3.com=103; __jdv=122270672|baidu-pinzhuan|t_288551095_baidupinzhuan|cpc|0f3d30c8dba7459bb52f2eb5eba8ac7d_0_d5c0bf4597784af39626f9dc96ef8725|1525777613180; shshshfp=cf94451de394accad5b53277cd3aa4ee; shshshsID=f40121f3221dd0417dfe24bcde68582a_3_1525777619489; __jdb=122270672.7.1977135510|2.1525777593; userInfoaccountclouds=1",
#         "Host": "home.jd.com",
#         "Referer": "https://www.jd.com/?cu=true&utm_source=baidu-pinzhuan&utm_medium=cpc&utm_campaign=t_288551095_baidupinzhuan&utm_term=0f3d30c8dba7459bb52f2eb5eba8ac7d_0_d5c0bf4597784af39626f9dc96ef8725",
#         "Upgrade-Insecure-Requests": "1",
#         "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.139 Safari/537.36",
#     }
#     request = Request('https://home.jd.com/',headers=un_hender)
#     html = urlopen(request)
#     print(html.read().decode('utf-8'))

def main():
    un_hender = {
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
        "Accept-Language": "zh,zh-CN;q=0.9,en;q=0.8,zh-HK;q=0.7,zh-TW;q=0.6",
        "Cache-Control": "max-age=0",
        "Connection": "keep-alive",
        "Cookie": "__jdu=1977135510; PCSYCityID=1; unpl=V2_ZzNtbRdTERQmX0NQcx9aDGJTRV9KUEASIgATBnMeCFJuBRFZclRCFXwUR1BnGFUUZwsZXEVcQBVFCHZXchBYAWcCGllyBBNNIEwHDCRSBUE3XHxcFVUWF3RaTwEoSVoAYwtBDkZUFBYhW0IAKElVVTUFR21yVEMldQl2VHMfWgVlBxZdQ2dzEkU4dlR4GVoNbzMTbUNnAUEpDUJceRFYSGcLFFtCVUcRdQl2VUsa; CCC_SE=ADC_xvgjOAgT%2fpXeR%2bWMyHxk%2fgHlIIaAxLAdVq8QA3kT7p%2fmMMRqBU%2fQ71sU6khge2lKs095aR%2bIWJHPb%2bLzMsR41tWN%2f2ff68VgYIUII6%2b1JUnkkI%2bt0J%2bi0B0bdDPMFYAeJxy0SdNe2A2CD%2bv8ik0WOpqfFqBaIkA%2fkQ2zY4gMHCfq7%2bKR%2beYB0vRxUNnJLdriwc76d1ooZw2OJzWDkJMPFxlO5wEjZoCyTcszEAiq%2b9Qn78O2e%2fy1cdAuxa2zrHL7blJqR0djL%2fIqPNvqoXgZF3xogsv1GC8phEpJ800uI%2fNOb6NPtLjWNfWHj5TaG%2fZC0jfolXyo4LKWexDDmd3jTVO6Sb4SzYhGD%2bGXeZ%2fBcMugaMae80nVlP0qF10BO37ARZ5jsCw5r%2fqw%2bIAsk5GT6lRY%2fJ5%2bMshZwm2hG7xOT%2fahDlbY6x%2faoeKskaBrJ595hys9hicckqOPflME3Zm9nBu88%2faf5C1eIEj5BCk4Ia2URVFa43DX5ZlFOCtj4kZUAKDGbInHg35CTUJ8McIDddQIpDrvGkEnMLVyQAgocDTtZUBo3sjiDDcaEgjJnJf4; __jda=122270672.1977135510.1525749724.1525749725.1525777593.2; __jdc=122270672; shshshfpa=d87a5592-c3b9-dc19-f153-95f78c52021a-1525777595; shshshfpb=095858767daf647b15660045411c69ad1a490e57cfbc697f95af184b5e; cid=NWJFMzUwNnlKMzU0N2pYNjk4OHZPMDcyMXBPMzMwMnVDNjc0M2lRMjE2NGdPNTM4; _jrda=1; _jrdb=1525777605046; 3AB9D23F7A4B3C9B=ZVK5XTXGGQMTEPBDC4ZD3TTM2IXFIGYBJIH2HCKHANV2XOZGJ72TREQAFWCKKAOIGTI7H3VACCKWOTEUHRLO5ON2SU; wlfstk_smdl=gz44fm0s1n5n2xzem0as0r48kpq5let1; TrackID=1LB5tEWkI0YBgNjdNqQpaeS4EmGMw8hACL-RW1ihbKEI4gRH2d5KA67eR-JPwMc6yY7okt-KSRzjYEcf9o0npBs9GPbv119MEt3PVedyd--RGgYZMJKdig2XXBTwKhp7V; pinId=TYeoPsPRbF4R-DoDjWKMVQ; pin=15853129020_p; unick=WitheK; thor=5F9F41A19B6F78B9E414FE39AFFF94523C4607D4EB5FCE0227D7C2E44744258B7A5F8294F2D5AF678B4D6C948FB1BD2031E0FBD93FA12FC381932DE4BF9C48D42CCAA2FD2B6961705064BE4A9118746DA7A7A7E6E0269B929CC3C057AF328EDE19A306C22625E0F13DF957EEF7DB872DD366ABA315730BD39CE3542D808AFA468C22F3A02B7505348117BE703371E6D7; _tp=zsVAGnJ5E6TLA%2Bmfte%2FKyA%3D%3D; _pst=15853129020_p; ceshi3.com=103; __jdv=122270672|baidu-pinzhuan|t_288551095_baidupinzhuan|cpc|0f3d30c8dba7459bb52f2eb5eba8ac7d_0_d5c0bf4597784af39626f9dc96ef8725|1525777613180; shshshfp=cf94451de394accad5b53277cd3aa4ee; shshshsID=f40121f3221dd0417dfe24bcde68582a_3_1525777619489; __jdb=122270672.7.1977135510|2.1525777593; userInfoaccountclouds=1",
        "Host": "home.jd.com",
        "Referer": "https://www.jd.com/?cu=true&utm_source=baidu-pinzhuan&utm_medium=cpc&utm_campaign=t_288551095_baidupinzhuan&utm_term=0f3d30c8dba7459bb52f2eb5eba8ac7d_0_d5c0bf4597784af39626f9dc96ef8725",
        "Upgrade-Insecure-Requests": "1",
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.139 Safari/537.36",
    }
    html = requests.get('https://home.jd.com/',headers=un_hender)
    print(html.text)

if __name__ == '__main__':
    main()