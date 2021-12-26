import requests
import json

# 获取药监总局化妆品详情数据

# 获取id地址
url = 'http://scxk.nmpa.gov.cn:81/xk/itownet/portalAction.do?method=getXkzsList'
# UA伪装
header = {
    'User-Agent' :'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.81 Safari/537.36'
}
# 存储id
id_list = []
#存储详情页信息
all_detail_list = []
# 参数
for page in range(1,6):
    page = str(page)
    data = {
        'on': 'true',
        'page': page,
        'pageSize': 15,
        'productName': '',
        'conditionType': 1,
        'applyname': '',
        'applysn': ''
    }
    # 发送post请求
    json_ids = requests.post(url=url,data=data,headers = header).json()

    # 遍历json_ids
    for dic in json_ids['list']:
        id_list.append(dic['ID'])
    print(len(id_list))


#查询详情url
detils_url = 'http://scxk.nmpa.gov.cn:81/xk/itownet/portalAction.do?method=getXkzsById'
for id in id_list:
    params = {
        'id':id
    }
    detail_json = requests.post(url=detils_url,params=params,headers=header).json()
    all_detail_list.append(detail_json)
#持久化存储
fileName = 'detail.json'
with open(fileName,'w',encoding="utf-8") as fp:
    json.dump(all_detail_list,fp=fp,ensure_ascii=False)
print(all_detail_list)
