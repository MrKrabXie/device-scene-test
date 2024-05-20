import os.path

import pytest

from utils.PathUtil import PathUtil

if __name__ == "__main__":
    rootDir = PathUtil.get_project_root()

    # 调用 pytest.main() 执行测试，并指定报告文件路径为 reports/login/login.html
    pytest.main(["../tests/login/test_login.py", "--html="+os.path.join(rootDir, "reports/login/login.html")])
