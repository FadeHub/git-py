import requests
from lxml import etree

# 使用xpath 爬取58二手房标题信息

url = 'https://bj.58.com/ershoufang/'
headers = {
    'User-Agent' :'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.81 Safari/537.36'
}
page_text = requests.get(url=url,headers=headers).text
tree = etree.HTML(page_text)
div_list = tree.xpath('//section[@class="list"]/div')
fp = open('58.txt','w',encoding='utf-8')
for div in div_list:
    title = div.xpath('./a//h3/@title')[0]
    print(title)
    fp.write(title+'\n')