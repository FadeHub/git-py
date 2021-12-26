import requests
import json

# 爬取豆瓣高分电影

# 爬取豆瓣电影url
url = 'https://movie.douban.com/j/search_subjects'
# UA伪装
header = {
    'User-Agent' :'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.81 Safari/537.36'
}
# 输入参数
kw = input("enter the page_start：")
# 组装参数
para = {
    'type': 'movie',
    'tag': '豆瓣高分',
    'sort': 'recommend',
    'page_limit': '20',
    'page_start': kw
}
# 发送get请求
response = requests.get(url=url,params=para,headers=header)
#返回json数据
list_json = response.json()
#持久化数据
fileName = kw + ".json"
fp = open(fileName,'w',encoding='utf-8')
json.dump(list_json,fp=fp,ensure_ascii=False)
print("over")