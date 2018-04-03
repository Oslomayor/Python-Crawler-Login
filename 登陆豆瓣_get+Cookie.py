# get + Cookie 方法登陆豆瓣 https://www.douban.com/
# get Request URL: https://www.douban.com/
# 12:47PM, Apr 3rd, 2018 @ Dorm
# Chrom 查看 Cookie , Cookie 添加到请求头里面


import requests
from bs4 import BeautifulSoup

url = 'https://www.douban.com/'
headers = {
    'Cookie':'bid=1ZCUYJaPiWE; __utmz=30149280.1520389985.3.3.utmcsr=cn.bing.com|utmccn=(referral)|utmcmd=referral|utmcct=/; ll="118172"; __utmc=30149280; ps=y; ue="du82774332@163.com"; push_noty_num=0; push_doumail_num=0; __utmv=30149280.17635; ap=1; _ga=GA1.2.227505494.1519225000; _gid=GA1.2.1213218516.1522726679; _pk_ref.100001.8cb4=%5B%22%22%2C%22%22%2C1522729153%2C%22https%3A%2F%2Fcn.bing.com%2F%22%5D; __utma=30149280.227505494.1519225000.1522726091.1522729158.5; dbcl2="176355602:QRXmxarPzls"; ck=yN-H; _pk_id.100001.8cb4=65f36aa18a798fcc.1520220460.4.1522729180.1522726681.'
}
res = requests.get(url, headers=headers)
soup = BeautifulSoup(res.text, 'html.parser')
# 用 BeautifulSoup 库输出格式化的 HTML 文档
print(soup.prettify())