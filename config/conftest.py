# conftest.py

import pytest

@pytest.fixture(scope="session")
def global_data():
    # 初始化全局数据，例如存储 Cookie 的字典
    global_data = {"cookies": {}}
    return global_data


