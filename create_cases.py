import os

# 确保testcases目录存在
os.makedirs("testcases", exist_ok=True)

cases = {
    "basic_get.yml": """config:
  name: "基础GET请求测试"
  base_url: "http://www.httpbin.org"

teststeps:
- name: "验证GET请求"
  request:
    method: GET
    url: /get
  validate:
  - eq: [status_code, 200]
  - eq: ["body.url", "http://www.httpbin.org/get"]
""",
    
    "post_with_params.yml": """config:
  name: "POST请求测试"
  base_url: "http://www.httpbin.org"
  variables:
    username: "testuser"

teststeps:
- name: "发送POST请求"
  request:
    method: POST
    url: /post
    json:
      user: "$username"
      timestamp: "2024-01-30"
  validate:
  - eq: [status_code, 200]
  - eq: ["body.json.user", "testuser"]
""",
    
    "check_headers.yml": """config:
  name: "响应头测试"
  base_url: "http://www.httpbin.org"

teststeps:
- name: "检查响应头"
  request:
    method: GET
    url: /headers
  validate:
  - eq: [status_code, 200]
  - contains: ["body.headers.Host", "www.httpbin.org"]
"""
}

for filename, content in cases.items():
    filepath = os.path.join("testcases", filename)
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"✓ 已创建: {filepath}")

print("\n✅ Day 2 所有用例已生成！")
print("运行测试: hrun testcases/")