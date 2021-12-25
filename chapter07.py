import requests
import json

#输入单词 返回翻译结果

# 指定url
url = 'https://fanyi.baidu.com/sug'
# UA伪装
header = {
    'User-Agent' :'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.81 Safari/537.36'
}
# post请求参数处理
kw = input('enter a word：')
data = {
    'kw':kw
}
# 发送请求
response = requests.post(url=url,data=data,headers=header)
# 获取响应结果，返回json
json_obj = response.json()
#持久化
fileName = kw + '.json'
fp = open(fileName,'w',encoding='utf-8')
json.dump(json_obj,fp=fp,ensure_ascii=False)
print("over!")