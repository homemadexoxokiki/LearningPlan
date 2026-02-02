# LearningPlan
介绍：
HttpRunner 是一款面向 HTTP(S) 协议的通用测试框架，只需编写维护一份 YAML/JSON 脚本，即可实现自动化测试、性能测试、线上监控、持续集成等多种测试需求

安装：pip install httprunner
安装 HttpRunner 后，以下 5 个命令会写入系统环境变量配置。
httprunner：主命令，用于所有功能。
hrun：指令 httprunner run 的别名，用于运行 YAML/JSON/Pytest 测试用例。
hmake: 指令 httprunner make 的别名，将 YAML/JSON 用例转换成 pytest 用例。
har2case：指令 httprunner har2case 的别名，将 HAR 文件转换成 YAML/JSON 用例。
locust：利用 locust 运行性能测试。

创建项目：
httprunner startproject 项目名
run运行实例
httprunner run testcase
