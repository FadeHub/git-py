import requests
import json

# 爬取kfc门店地址
# 爬取url地址
url = 'http://www.kfc.com.cn/kfccda/ashx/GetStoreList.ashx?op=keyword'

# UA伪装
header = {
    'User-Agent' :'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.81 Safari/537.36'
}
json_list = []
# 输入参数
kw = input("enter the keywords：")
# 组装参数
for page in range(1,7):
    page = str(page)
    para = {
        'cname': '',
        'pid': '',
        'keyword': kw,
        'pageIndex': page,
        'pageSize': '10'
    }
    # 发送post请求
    obj = requests.post(url=url,params=para,headers=header).json()
    json_list.append(obj)

#持久化数据
fileName = "address.json"
with open(fileName,'w',encoding="utf-8") as fp:
    json.dump(json_list,fp=fp,ensure_ascii=False)
print("over")