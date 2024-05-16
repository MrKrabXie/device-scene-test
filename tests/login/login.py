import unittest


# class MyTestCase(unittest.TestCase):
#     def test_something(self):
#         self.assertEqual(True, False)  # add assertion here

import requests

def test_login():
    # 请求的URL
    url = "http://192.168.10.110:8080/cognition/rest/login"

    # 请求的JSON数据
    data = {
        "loginType": "doc_uname_pass",
        "username": "fe_xmj",
        "password": "888888"
    }

    # 发送POST请求
    response = requests.post(url, json=data)

    # 获取响应状态码和响应内容
    status_code = response.status_code
    response_data = response.json()
    cookie = response.cookies
    # 打印结果
    print("Status Code:", status_code)
    print("Response Data:", response_data)

    # 断言响应状态码为200
    assert status_code == 200

    # 断言响应中包含特定的信息
    assert "JSESSIONID" in cookie
    assert "success" in response_data


if __name__ == '__main__':
    test_login()