# device-scene-test

python + requests + pytest + json + 断言库 + Mock + 报告生成工具 + 持续集成工具
1. **Requests库**：Requests是Python中用于发送HTTP请求的简单而强大的库。它易于学习和使用，并且提供了丰富的功能，如发送GET、POST请求、设置请求头、处理响应等。

2. **pytest框架**：Pytest是一个灵活、强大的Python测试框架，支持参数化测试、fixture、自动发现测试用例等功能。它易于扩展，并且提供了丰富的插件生态系统。

3. **JSON库**：Python自带的json模块可以帮助你解析和构建JSON数据，这在处理API的请求和响应时非常有用。

4. **断言库**：Python的内置断言功能足以满足基本的断言需求，但你也可以选择使用第三方的断言库，如Pytest的assert断言、unittest框架的assertions或者Hypothesis库。

5. **Mock库**：在测试过程中，模拟一些外部依赖（如其他服务、数据库）是很常见的需求。Python的unittest.mock库提供了方便的工具来模拟对象和行为，帮助你进行单元测试和集成测试。

6. **报告生成工具**：Allure、pytest-html等工具可以生成漂亮的HTML测试报告，展示测试结果、失败原因和执行时间等信息。

7. **持续集成工具**：与CI/CD工具集成，如Jenkins、GitLab CI、Travis CI等，可以实现自动化构建、测试和部署。

以上是一些常用的Python技术和工具，可以帮助你构建高效的接口自动化测试项目。根据项目需求和团队经验，你可以灵活选择并结合使用这些工具。


python版本选用：3.10版本

# device-scene-test

## 目录结构

```bash  
device-scene-test/  
│  
├── tests/                          # 测试代码目录  
│   ├── test_case1.py               # 测试用例文件1  
│   ├── test_case2.py               # 测试用例文件2  
│   └── ...  
│  
├── data/                           # 测试数据目录  
│   ├── test_data.json              # 测试数据文件  
│   ├── ...  
│  
├── config/                         # 配置文件目录  
│   ├── config.py                   # 项目配置文件  
│   ├── ...  
│  
├── utils/                          # 工具类目录  
│   ├── api_client.py               # 封装HTTP请求的客户端类  
│   ├── data_reader.py              # 读取测试数据的类  
│   ├── logger.py                   # 日志记录类  
│   ├── assertions.py               # 自定义断言类  
│   ├── ...  
│  
├── reports/                        # 测试报告目录  
│   ├── test_report.html            # 测试报告文件  
│   ├── ...  
│  
├── requirements.txt                # 项目依赖文件  
└── README.md                       # 项目说明文件
