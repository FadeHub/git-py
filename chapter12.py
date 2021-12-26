import requests
from bs4 import BeautifulSoup

#使用BeautifulSoup 解析匹配
# 爬取https://www.shicimingju.com/book/sanguoyanyi.html 三国演义章节标题和章节内容

url = 'https://www.shicimingju.com/book/sanguoyanyi.html'
# UA伪装
header = {
    'User-Agent' :'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.81 Safari/537.36'
}

response = requests.get(url=url,headers=header)
response.encoding = 'utf-8'
print(response.encoding)
page_text = response.text
#实例化BeautifulSoup对象
soup = BeautifulSoup(page_text,'lxml')
#解析章节标题和详情页url
li_list = soup.select('.book-mulu > ul > li')
fp = open('sanguoyanyi.txt','w',encoding='utf-8')
for li in li_list:
    title = li.a.string
    detail_url = 'https://www.shicimingju.com' + li.a['href']
    #解析详情内容
    detail_page_text_reponse = requests.get(url=detail_url,headers=header)
    detail_page_text_reponse.encoding = 'utf-8'
    detail_page_text = detail_page_text_reponse.text
    detail_soup = BeautifulSoup(detail_page_text,'lxml')
    div_tag = detail_soup.find('div',class_='chapter_content')
    #解析章节内容
    context = div_tag.text
    fp.write(title + ':' +context +'\n')
    print(title,'爬取成功！！！')