import requests
import re


def get_page(page):
    url = "http://www.qiushibaike.com/hot/page/" + str(page) + "/"
    user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
    headers = {'User-Agent': user_agent}
    QSBK = requests.get(url, headers=headers)
    return QSBK.text


def get_msg(data):
    pattern = '<div.*?class="content">(.*?)<!--.*?-->.*?</div>'
    items = re.findall(pattern, data, re.S)
    item = []
    for item in items:
        print(item)


def start(i):
    print("如需继续浏览下一页，请输入Y并按回车！")
    temp = input()
    if temp == "Y" or 'y':
        date = get_page(i)
        get_msg(date)
        start(i + 1)

    else:
        print("程序结束！")


start(1)
