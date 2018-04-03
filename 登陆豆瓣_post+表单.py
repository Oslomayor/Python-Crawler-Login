# POST 方法登陆豆瓣 https://www.douban.com/
# POST Request URL: https://www.douban.com/accounts/login
# 11:40AM, Apr 3rd, 2018 @ Dorm
# Chrom 查看 post 数据的方法

import requests
from bs4 import BeautifulSoup

headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) \
AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'}

url = 'https://www.douban.com/accounts/login'
data = {
    'source':'index_nav',
    'form_email':'du82774332@163.com',
    'form_password':'!db12345679'
}
res = requests.post(url, data=data)
soup = BeautifulSoup(res.text, 'html.parser')
# 用 BeautifulSoup 库输出格式化的 HTML 文档
print(soup.prettify())