# 1、导包  爬虫模块
import requests
import re
import csv

with open('排名.csv', 'a', encoding='utf-8', newline='')as f:
    csv_writer = csv.writer(f)
    csv_writer.writerow(["country", "rank_display", "ind_0", "ind_1", "ind_2", "rank_d_0", "rank_d_1", "rank_d_2", "university"])
def replace(str):
    str=re.sub('<.*?>','',str)
    return str
# 2、确定网址
url='https://www.qschina.cn/sites/default/files/qs-rankings-data/cn/2122636.txt?_=1671018565951'
# 3、爬虫的伪装  反爬
headers = {
    # 身份信息  个人账户再浏览器上面的访问信息
    'cookie': '__gads=ID=168665f3b67b4052:T=1670824297:S=ALNI_MZl9Ky7fFsyTeFi6iOTUclJ_ObGKQ; _ga=GA1.2.1912919503.1670824298; _gid=GA1.2.52333245.1670824298; cookie-agreed-version=1.0.0; _hjSessionUser_1833300=eyJpZCI6IjJjMzNiMzM4LTBjN2QtNTk5Yy04MjI4LWUyZTA5ODU1MDdkZSIsImNyZWF0ZWQiOjE2NzA4MjQzMDEzNzMsImV4aXN0aW5nIjp0cnVlfQ==; cookie-agreed=2; Hm_lvt_e479a6c6846597fcef51b3d40cfae443=1670824845,1670908459,1670919203,1670993534; __gpi=UID=00000b8ee61c511c:T=1670824297:RT=1671016560:S=ALNI_Mb9b_xY-9to0eAcZw9NB_bjpO6FtA; _hjSession_1833300=eyJpZCI6IjdhYTQwMGJiLTc3N2UtNDVmMy05M2ZkLTlmMGEzYzcxZjJmYiIsImNyZWF0ZWQiOjE2NzEwMTY1NjMyOTUsImluU2FtcGxlIjpmYWxzZX0=; _hjAbsoluteSessionInProgress=0; _hjIncludedInSessionSample=0; Hm_lpvt_e479a6c6846597fcef51b3d40cfae443=1671018566',
    # 防盗链   网页的原始信息
    'referer': 'https://www.qschina.cn/',
    # 用户代理  浏览器的唯一标识
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.0.0 Safari/537.36',
}
# 4、发送请求
response=requests.get(url=url,headers=headers)
# 5、响应数据   {} 字典
# print(response.json())
# 6、解析数据  字典键值对取值
json=response.json()['data']
# print(json)
for data in json:
    country=data['country']
    rank_display = data['rank_display']
    ind_0=replace(data['ind_0'])
    ind_1=replace(data['ind_1'])
    ind_2=replace(data['ind_2'])
    rank_d_0=replace(data['rank_d_0'])
    rank_d_1=replace(data['rank_d_1'])
    rank_d_2=replace(data['rank_d_2'])
    university=replace(data['title'])
    print(country,rank_display,ind_0,ind_1,ind_2,rank_d_0,rank_d_1,rank_d_2,university,sep='|')
    with open('排名.csv','a',encoding='utf-8',newline='')as f:
        csv_writer=csv.writer(f)
        csv_writer.writerow([country,rank_display,ind_0,ind_1,ind_2,rank_d_0,rank_d_1,rank_d_2,university])
