import requests

#要访问的url
url = "https://www.baidu.com/s"
#UA 伪装成刘浏览器
header = {
    'User-Agent' :'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.81 Safari/537.36'
}
#输入要查询的关键字
kb = input("enter the word：")
#查询参数关键字
param = {
    "wd":kb
}
#发送请求返回response
reponse = requests.get(url=url,params=param,headers=header)
#请求返回字符转
page_text = reponse.text
#保存返回字符串名字
fileName = kb + '.html'
with open(fileName,'w',encoding="utf-8") as fb:
    fb.write(page_text)
print(fileName,'保存成功')