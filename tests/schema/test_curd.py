
import pytest
import requests

from tests.login import test_login


@pytest.fixture(scope="function")
def cookies():
    # 在测试方法执行前获取 cookies
    response = test_login.getCookie()
    cookies = response.cookies
    return cookies


# 这里的data 和 配置， 都要抽出去
def test_save_plans(cookies):
    # 定义请求头
    headers = {
        "User-Agent": "Apifox/1.0.0 (https://apifox.com)",
        "Content-Type": "application/json",
        "Accept": "*/*",
        "Host": "192.168.10.110:8080",
        "Connection": "keep-alive",
    }

    # 定义请求体
    data = {
        "sftj00": 1,
        "sfyx00": 1,
        "sysj00": 60,
        "xzsj00": 60,
        "famc00": "1407测试重复问题2",
        "refId": "",
        "schemaDetail": "111",
        "trainFrequency": 1,
        "trainCycle_unit": "日",
        "trainCycle": 3,
        "lowTrainTime": 4,
        "highTrainTime": 30,
        "validStartDate": "2024-05-10 00:00:00",
        "blh000": "430202198602103913",
        "brid00": "225a912f-0543-4e39-9eec-ae2a9d60c367",
        "projectList": [
            {
                "xlmc00": "反应速度训练",
                "xlid00": "jdfysxl",
                "mbdj00": 1,
                "mbts00": 10
            }
        ],
        "deleteList": [],
        "saveType": 0
    }

    # 发送 POST 请求
    response = requests.post('http://192.168.10.110:8080/cognition/choosepro/savePlans.htm', headers=headers, cookies=cookies, json=data)

    # 检查响应状态码
    assert response.status_code == 200




def test_update_plans(cookies):
    print("testDelete")

def test_detail_plans(cookies):
    print("test_detail_plans")

