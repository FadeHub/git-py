import requests
import json

# 爬取豆瓣电影高分电影
url = 'https://movie.douban.com/j/search_subjects'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.81 Safari/537.36'
}
for page_start in range(1,3):
    data = {
        'type': 'movie',
        'tag': '豆瓣高分',
        'sort': 'time',
        'page_limit': 20,
        'page_start': page_start
    }
    response = requests.get(url=url,params=data,headers=headers)
    movie_json = response.json()
    #json_str = json.dump(content_json)
    print(movie_json)