import requests
from lxml import etree

# 爬取58租房信息
headers = {
    'User-Agent' :'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.81 Safari/537.36'
    }
url = "https://bj.58.com/chuzu/pn{0}/?PGTID=0d3090a7-0000-1840-3c31-74c281b4647c&ClickID=3"
# 58租房url
fp = open('58租房.txt','w',encoding='utf-8')
for page in range(1,5):
    page = str(page)
    new_url = url.format(page)
    page_text = requests.get(url=url,headers=headers).text
    tree = etree.HTML(page_text)
    li_list = tree.xpath('//ul[@class="house-list"]/li')
    for li in li_list:
        house_detail = li.xpath('./div[@class="des"]//text()')
        house_detail = ''.join(house_detail).replace("\n",' ').replace(" ",'')
        house_price = li.xpath('./div[@class="list-li-right"]//b[@class="strongbox"]/text()')
        house_price = ''.join(house_price)
        fp.write(house_detail + '========>' + house_price+'\n')
        print(house_detail + "========>" + house_price)