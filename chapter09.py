import requests
import json

# 爬取kfc门店地址
# 爬取url地址
url = 'http://www.kfc.com.cn/kfccda/ashx/GetStoreList.ashx?op=keyword'

# UA伪装
header = {
    'User-Agent' :'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.81 Safari/537.36'
}
# 输入参数
kw = input("enter the keywords：")
# 组装参数
para = {
    'cname': '',
    'pid': '',
    'keyword': kw,
    'pageIndex': '1',
    'pageSize': '10'
}
# 发送get请求
response = requests.post(url=url,params=para,headers=header)
#返回json数据
list_text = response.text
#持久化数据
fileName = kw + ".json"
with open(fileName,'w',encoding="utf-8") as fb:
    fb.write(list_text)
print("over")