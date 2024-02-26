import requests
import re
import csv

def replace(str_):
    str_ = re.findall('<div class="td-wrap"><div class="td-wrap-in">(.*?)</div></div>', str_)[0]
    return str_

with open('rank.csv', mode='a', encoding='utf-8', newline='') as f:
    csv_writer = csv.writer(f)
    csv_writer.writerow(['country', 'rank', 'region', 'score_1', 'score_2', 'score_3', 'score_4', 'score_5', 'score_6', 'stars', 'total_score', 'university', 'year'])
url = 'https://www.qschina.cn/sites/default/files/qs-rankings-data/cn/2057712_indicators.txt'
response = requests.get(url=url)
json_data = response.json()
data = json_data['data']
for i in data:
    country = i['location'] # 国家/地区
    rank = i['overall_rank']    # 排名
    region = i['region']    # 大洲
    score_1 = replace(i['ind_76'])  # 学术声誉
    score_2 = replace(i['ind_77'])  # 雇主声誉
    score_3 = replace(i['ind_36'])  # 师生比
    score_4 = replace(i['ind_73'])  # 教员引用率
    score_5 = replace(i['ind_18'])  # 国际教室
    score_6 = replace(i['ind_14'])  # 国际学生
    stars = i['stars']  # 星级
    total_score = replace(i['overall']) # 总分
    university = i['uni']   # 大学
    university = re.findall('<div class="td-wrap".*?class="uni-link">(.*?)</a></div></div>', university)[0]
    year = "2022"   # 年份
    print(country, rank, region, score_1, score_2, score_3, score_4, score_5, score_6, stars, total_score, university, year)
    with open('rank.csv', mode='a', encoding='utf-8', newline='') as f:
        csv_writer = csv.writer(f)
        csv_writer.writerow([country, rank, region, score_1, score_2, score_3, score_4, score_5, score_6, stars, total_score, university, year])
        """
        打字是肯定有打的
        """