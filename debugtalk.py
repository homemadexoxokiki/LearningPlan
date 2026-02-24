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
  
