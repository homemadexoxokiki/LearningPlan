import time
import hashlib
import random
from datetime import datetime

#1.基础工具函数
def get_current_time():
  """"获取当前时间戳"""
  return datetime.now().strftime("%Y-%m-%d %H:%M:%S")

def generate_random_string(length=8):
  """生成随机字符串"""
  import string
  return ''.join(random.choices(string.ascii_letters + string.digits, k=length))

#2.数据处理函数
def calculate_md5(text):
  """计算MD5值"""
  return hashlib.md5(text.encode()).hexdigest()

def build_user_data(username, age):
  ""构造用户数据""
  return{
    "username": username,
    "age": age,
    "timestamp": get_current_time(),
    "user_id": generate_random_string(10)
}

#断言辅助函数
def check_response_time(response_time, threshold=1000):
  ""检查响应时间是否在阈值内""
  return response_time <= threshold

def validate_status_code(status_code, expected_codes=[200,201]):
  ""验证状态码是否在预期列表中""
  retrun status_code in expected_codes
  
