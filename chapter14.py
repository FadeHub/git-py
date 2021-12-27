import requests
from lxml import etree
import os

url = 'https://pic.netbian.com/4kyouxi/'
headers = {
    'User-Agent' :'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.81 Safari/537.36'
}
page_text = requests.get(url=url,headers=headers).text
tree = etree.HTML(page_text)
if not os.path.exists('picLibs'):
    os.mkdir('picLibs')
li_list = tree.xpath('//div[@class="slist"]/ul/li')
for li in li_list:
    img_src = 'https://pic.netbian.com/'+li.xpath('./a/img/@src')[0]
    img_name = li.xpath('./a/img/@alt')[0]
    img_name = img_name.encode('iso-8859-1').decode('gbk')
    img_data = requests.get(img_src,headers).content
    img_path = 'picLibs/' + img_name + '.jpg'
    print(img_src + ' ' + img_name)
    with open(img_path,'wb') as fp:
        fp.write(img_data)
        print(img_name+ '：'+'下载成功！')
