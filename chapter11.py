import requests
import os
import re

# 爬取糗事百科视频 使用正则表达式匹配
# 糗事百科视频
if not os.path.exists("D:/qiushibaike"):
    os.mkdir("D:/qiushibaike")
url = 'https://www.qiushibaike.com/video/{0}/'
# UA伪装
header = {
    'User-Agent' :'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.81 Safari/537.36'
}
for page in range(1,3):
    page = str(page)
    new_url = url.format(page)
    page_text = requests.get(url=new_url,headers = header).text
    #使用正则表达式匹配
    ex = '<video controls="controls" preload="meta" width="100%">.*?<source src="(.*?)" type=.*?</video>'
    video_list = re.findall(ex,page_text,re.S)
    for src in video_list:
        #拼装完整url
        src = "https:" + src
        print('视频地址：'+src)
        #请求视频二进制数据
        video_data = requests.get(url=src,headers=header).content
        #生成视频名称
        video_name = src.split('/')[-1]
        print('视频名字：'+video_name)
        #视频存储路径
        video_path = 'D:/qiushibaike/' + video_name
        print('视频存储路径：'+video_path)
        with open(video_path,'wb') as fp:
            fp.write(video_data)
            print("下载完成！")

