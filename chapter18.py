import requests
from lxml import etree

url = 'https://bj.zuke.com/fang/index1.html'
headers = {
    'User-Agent' :'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.81 Safari/537.36'
}
page_text = requests.get(url=url,headers=headers).text
tree = etree.HTML(page_text)
a_list = tree.xpath('//div[@class="list"]/a')
for a in a_list:
   title = a.xpath('./div[@class="list-img"]/img/@alt')
   title = ''.join(title)
   house_detail = a.xpath('./div[@class="list-info"]//text()')
   house_detail = ''.join(house_detail).replace("\n", ' ').replace(" ", '')
   print(title + "=======>" + house_detail)