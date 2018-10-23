import requests,json
import unittest

class demo(unittest.TestCase):
    def setUp(self):
        #初始化信息
        self.url = "https://api.douban.com/v2/movie/search?q="
        self.book_name = "小王子"
        self.name = "圣-埃克苏佩里"

    def test_actor(self):
        req = requests.get(self.url+self.book_name)
        print(type(req))
        print("==========================================================================")
        print(req.json())
        req=json.dumps(req.json(), ensure_ascii=False, indent=4 )
        self.assertIn(self.book_name, req ,msg=None)

    if __name__ == '__main__':
        unittest.main()
# import requests,json
# import unittest
#
# class demo(unittest.TestCase):
#     def setUp(self):
#         # 初始化信息
#         self.url = "https://api.douban.com/v2/movie/search?"
#         self.actor_name = "q=TomCruise"
#         self.style_tag = "tag=爱情"
#         self.name = "汤姆·克鲁斯"
#         self.action = "动作"
#
#     def test_actor(self):
#         # 执行测试
#         req = requests.get(self.url + self.actor_name) # 通过requests 发起请求
#         req = json.dumps(req.json(), ensure_ascii=False, indent=4)
#         self.assertIn(self.name, req, msg=None) # 检查有没有 "汤姆·克鲁斯"这个演员
#
#     def test_style_tag(self):
#         # 执行测试
#         req = requests.get(self.url + self.actor_name) # 通过requests 发起请求
#         req = json.dumps(req.json(), ensure_ascii=False, indent=4)
#         self.assertIn(self.action, req, msg=None) # 检查有没有 "动作片"
#
# if __name__ == '__main__':
#     unittest.main()