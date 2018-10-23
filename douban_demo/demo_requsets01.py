# import requests
# book_name = "q=小王子"
# url = "https://api.douban.com/v2/book/search?"
# req = requests.get(url+book_name) # 通过requests 发起请求
# a = req.text
# print(a)
# if req.status_code == 200:
#     #req.status_code 就是HTTP的状态码
#     print("测试通过，请求已成功，请求所希望的响应头或数据体将随此响应返回")
# elif req.status_code == 404:
#     print("请求失败，返回404，请求所希望得到的资源未在服务器上发现")
#

# import requests, json
#
# url = "http://39.108.58.80:8080/aisales-service/aisales/listen"
# content = {"currentUtterance": "它的尺寸是多少", "deviceID": "a"}
# str_content = json.dumps(content)
# req = requests.post(url, json= content) # 通过requests 发起请求
# print(req.text)

import requests, json

url = "http://39.108.58.80:8080/aisales-service/aisales/listen"
content = {"currentUtterance": "它的尺寸是多少", "deviceID": "a"}
req = requests.post(url, json=content) # 通过requests 发起请求
print(req.text)
