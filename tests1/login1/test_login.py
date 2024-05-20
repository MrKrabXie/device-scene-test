import unittest


# class MyTestCase(unittest.TestCase):
#     def test_something(self):
#         self.assertEqual(True, False)  # add assertion here

import requests

from config.APISuffix import APISuffix
from config.EnviromentUrl import EnviromentUrl
# from config.APISuffix import APISuffix
# from config.EnviromentUrl import EnviromentUrl

# 在 test_login.py 文件的顶部添加以下导入语句

from utils.DataUtil import DataUtil
from utils.PathUtil import PathUtil


def test_loginBK():
    # 请求的URL
    # url = EnviromentUrl.TEST_BASE_URL + APISuffix.LOGIN_SUFFIX + "/login"
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



def test_login():
    # 请求的URL
    url = EnviromentUrl.TEST_BASE_URL + '/rest/' + APISuffix.LOGIN_SUFFIX
    # url = "http://192.168.10.110:8080/cognition/rest/login"

    # 请求的JSON数据
    file_path = PathUtil.get_success_directory(APISuffix.LOGIN_SUFFIX)
    loginData = DataUtil.get_credentials_from_file(file_path)
    print(loginData)

    # 发送POST请求
    response = requests.post(url, json=loginData)

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