from bs4 import BeautifulSoup
import requests
def main():
    headers = {"User-Agent":"Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko)Chrome/65.0.3325.146 Safari/537.36"}
    url = "https://hr.tencent.com/position.php?&start=10"
    html = requests.get(url,headers=headers)
    soup = BeautifulSoup(html.text,'lxml')
    even_list = soup.select('tr[class="even"]')
    odd_list = soup.select("tr[class='odd']")
    list_all = []
    for even in even_list:
        all_list = {}
        name = even.a.string
        url = even.a.attrs['href']
        job = even.select('td')[1].get_text()
        man = even.select('td')[2].get_text()
        address = even.select('td')[3].get_text()
        time = even.select('td')[4].get_text()
        all_list['name'] = name
        all_list['data_link'] = url
        all_list['job_category'] = job
        all_list['recruit_number'] = man
        all_list['address'] = address
        all_list['publish_time'] = time
        list_all.append(all_list)
    for odd in odd_list:
        all_list1 = {}
        name = odd.a.string
        url = odd.a.attrs['href']
        job = odd.select('td')[1].get_text()
        man = odd.select('td')[2].get_text()
        address = odd.select('td')[3].get_text()
        time = odd.select('td')[4].get_text()
        all_list1['name'] = name
        all_list1['data_link'] = url
        all_list1['job_category'] = job
        all_list1['recruit_number'] = man
        all_list1['address'] = address
        all_list1['publish_time'] = time
        list_all.append(all_list1)
    print(list_all)
if __name__ == '__main__':
    main()
