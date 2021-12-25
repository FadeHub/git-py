import requests

#step1：指定url
url = "https://www.bilibili.com/";
#step2：发起请求，get方法会返回一个对象
response = requests.get(url)
#step3：获取响应数据，返回字符串
page_text = response.text
print(page_text)
#step4：持久化数据
with open('D:/aplus/bilili.html','w',encoding='utf-8') as f:
    f.write(page_text)


