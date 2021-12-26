import requests
from lxml import etree

# 使用xpath 爬取58二手房信息

headers = {
    'User-Agent' :'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.81 Safari/537.36'
}
url = 'https://bj.58.com/ershoufang/{0}/?PGTID=0d30000c-0000-1bdc-b1e5-d9efea8142e9&ClickID=1'
for page in range(1,6):
    page = str(page)
    new_url = url.format(page)
    page_text = requests.get(url=new_url,headers=headers).text
    tree = etree.HTML(page_text)
    div_list = tree.xpath('//section[@class="list"]/div')
    fp = open('58.txt','w',encoding='utf-8')
    for div in div_list:
        title = div.xpath('./a//h3/@title')[0]
        roomsAndHalls = div.xpath('./a//div[@class="property-content-info"]//span/text()')
        address = div.xpath('./a//div[@class="property-content-info property-content-info-comm"]//span/text()')
        house_year = div.xpath('./a//span[@class="property-content-info-tag"]/text()')
        roomsAndHalls = ''.join(roomsAndHalls)
        address = ''.join(address)
        house_year = ''.join(house_year)
        # print(title)
        # print(''.join(roomsAndHalls))
        # print(''.join(address))
        # print(''.join(house_year))
        print(title+'======>'+roomsAndHalls+'======>'+address+'======>'+house_year)
        fp.write(title+'======>'+roomsAndHalls+'======>'+address+'======>'+house_year+'\n')