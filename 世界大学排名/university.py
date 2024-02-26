"""
python项目实战-采集世界大学排名信息、数据可视化分析
   python运用于生活  最新世界大学排行
带你了解国内外大学真实信息  看看你的母校上榜了没~

课程内容：
1、爬虫原理
2、正则解析式
3、动态数据抓包
4、字典取值

主讲老师：无言
时间：晚上19:30准时授课
开发环境：pycharm,python3+win11,requests
--------------------------------------------------------------------------------------------------------
环境模块安装：【第三方库】
    requests爬虫模块==》在pycharm上打开(终端)Terminal 输入命令行 pip install requests
    csv、re==》自带模块不需要安装

安装失败解决方法：【加镜像源】
    格式：pip install -i 源路径 安装的包名称

    清华：https://pypi.tuna.tsinghua.edu.cn/simple
    阿里云：http://mirrors.aliyun.com/pypi/simple/
    中国科技大学 https://pypi.mirrors.ustc.edu.cn/simple/
    华中理工大学：http://pypi.hustunique.com/
    山东理工大学：http://pypi.sdutlinux.org/
    豆瓣：http://pypi.douban.com/simple/
------------------------------------------------------------------------------------------------------------------------
pycharm如何安装插件?
    1.选择file(文件)>>> setting(设置)>>>Plugins(插件)
    2.点击 Marketplace输入想要安装的插件名字比如:翻译插件 输入Translation / 汉化插件 输入 Chinese
    3.选择相应的插件点击install(安装)即可
    4.安装成功之后是会弹出重启pycharm的选项点击确定，重启即可生效
--------------------------------------------------------------------------------------------------------------
python的应用学习方向有哪些？
    网站开发：
        如目前优秀的全栈的Django、框架flask，都继承了python简单、明确的风格，开发效率高、易维护，与自动化运维结合性好。
        python已经成为自动化运维平台领域的事实标准；
        python开发的网站：
            豆瓣 https://www.douban.com/
            YouTube，Dropbox，Facebook，知乎...等等
    爬虫开发：
        在爬虫领域，python几乎是霸主地位，将网络上一切的数据作为资源，通过自动化程序进行针对性的数据采集以及处理。
        从事领域应该学习爬虫策略、高性能异步IO流、分布式爬虫等，并针对scrapy框架源码进行深入剖析，从而理解其原理并
        实现自定义爬虫及其相关兼职案例。
    数据分析：
        python语言相对于其他解释性语言最大的特点是其庞大而活跃的科学计算生态，在数据分析、交互、可视化方面有相当完善和优秀的库。
    自动化脚本/运维/测试/办公：
        执行许多重复任务，例如阅读PDF、播放音乐、查看天气、打开书签、清理文件夹等等，
        使用自动化脚本就无需手动一次又一次地完成这些任务，非常方便
    人工智能：
        各种人工智能算法都基于python编写，尤其pytorch之后，python作为AI时代头牌语言的位置基本确定。作为被用于
        机器学习和人工智能系统以及各种现代技术的一门语言，Python能够十分容易地应用于分析和组成可用的数据，这也使
        它成为数据科学中最流行的语言之一。而丰富的本机拓展也使Python的优势得以强化，更适用于机器学习、数据计算和
        人工智能领域。
    游戏开发：
        Python有很好的3D渲染库和游戏开发框架，有很多实用Python开发的游戏，如迪士尼卡通城、黑暗之刃。
        常用PyGame、PyKyra等和一个PyWeek的比赛。对于想要进军游戏行业的同学们，Python也是一个不错的选择。
---------------------------------------------------------------------------------------------------------------
python找工作就业方向以及薪资待遇情况怎么样？
    python找工作方向主要是
        开发工程师<网站开发/全栈开发>
            -北京平均薪资23k
            -应届生 15k
            -1-3年 16.9k
            -3-5年 22.9k
            -数据来源：https://www.jobui.com/salary/beijing-python/
            招聘数据来源：(前程无忧招聘)https://search.51job.com/list/000000,000000,0000,00,9,99,Python,2,1.html?lang=c&postchannel=0000&workyear=99&cotype=99&degreefrom=99&jobterm=99&companysize=99&ord_field=0&dibiaoid=0&line=&welfare=
        爬虫工程师
            -北京平均薪资22.5k
            -应届生 16.7k
            -1-3年 18.1k
            -3-5年 24k
            -数据来源：https://www.jobui.com/salary/beijing-pachong/
            招聘数据来源：(前程无忧招聘)https://search.51job.com/list/000000,000000,0000,00,9,99,python%25E7%2588%25AC%25E8%2599%25AB,2,1.html?lang=c&postchannel=0000&workyear=99&cotype=99&degreefrom=99&jobterm=99&companysize=99&ord_field=0&dibiaoid=0&line=&welfare=
        数据分析师
            -.北京平均薪资253k
            -应届生 12.5k
            -1-3年 18k
            -3-5年 26.3k
            -数据来源：https://www.jobui.com/salary/beijing-shujufenxi/
            招聘数据来源：(前程无忧招聘)https://search.51job.com/list/000000,000000,0000,00,9,99,%25E6%2595%25B0%25E6%258D%25AE%25E5%2588%2586%25E6%259E%2590,2,1.html?lang=c&postchannel=0000&workyear=99&cotype=99&degreefrom=99&jobterm=99&companysize=99&ord_field=0&dibiaoid=0&line=&welfare=
---------------------------------------------------------------------------------------------------------------------------------------------------------------------
从零开始的接单流程全攻略？
1、资源整合   如何形成副业收入并且长期稳定
2、前置判断   合法性、可行性、投入产出
3、需求对接   文档化、确认需求和交付周期
4、押金支付   学院担保
5、项目开发同步进度
6、录屏演示功能
7、尾款结算
8、代码支付、数据交付
9、售后维护
---------------------------------------------------------------------------------------------------------------------------------------------------------------------
python想要做兼职外包是学习什么？
    外包是什么？是指别人花钱请你写程序，根据甲方的需求定制化开发程序软件，从而得到一定报酬
    目前关于爬虫开发+数据分析相对而言会多一些：
        比如：个人商家需要一些数据采集；某人公司需要特定数据等等
        采集电商平台数据/采集APP视频，音频数据/采集房源数据做可视化分析/采集招聘网站做可视化分析
        这些都是普遍的外包需求
    根据外包的需求程度以及难易程度  收费标准也是不一样的，按照分布计算
        初级外包：100-300左右     耗时：30-60分钟   三天
        中等外包：500+左右        耗时：1-2天     一周左右
        高级难度外包：1000+ 上不封顶   耗时3-5天不等   十天、半个月、一个月
    ******爬虫和数据分析外包 一般情况写外包的周期相对而言会短一些*******

    网站开发类外包难度相对会大些，同样的价格也会高很多
        比如开发后台数据管理系统/ 某公司企业官网 /或者学生毕设等等
    价格相对而言是更高的，网站开发普遍上千，大型系统网页开发金额上不封顶

    可以去哪里接兼职外包？
        -淘宝/闲鱼
        -外包接单群<会有一定的抽成>
        -公共开放的外包平台<需要押金和工作室或者公司担保>
            1、猿急送：https://www.yuanjisong.com/job
            2、猪八戒：https://changsha.zbj.com/sem/index
            3、程序员客栈：https://www.proginn.com/cat/
            4、云沃客：https://www.clouderwork.com/jobs/project.html
            5、开源众包：https://zb.oschina.net/projects/list.html
            6、一品威客：https://www.epwk.com/
            7、智诚外包网:http://www.taskcity.com/
            8、电鸭社区：https://eleduck.com/categories/13?page=1
            9、英选：https://www.yingxuan.io/
            10、实现网:https://shixian.com/jobs/part-time
--------------------------------------------------------------------------------------------------------------
课前准备：
    1.本节公开课时限两小时，请大家合理安排自己听课时间
    2.如有需要学习资料以及录播的同学，请添加助力老师小萧
    3.课程的专业性会比较高，大家有不懂的问题可以直接提出来。

------------------------------------------------------------------------------------------------------------------------
爬虫为主的案例： 零基础  0   有基础   2

一、爬虫基本概念：互联网定向采集数据的工具
实质：模拟浏览器 向服务器 发送请求

二、思路分析：通过开发者工具进行访问--》网络--》刷新--》全部--》搜索

三、代码编写：发送请求、返回数据、提取数据、保存数据
https://www.qschina.cn/sites/default/files/qs-rankings-data/cn/2122636.txt?_=1671018565951

'https://www.qschina.cn/sites/default/files/qs-rankings-data/cn/2122636.txt'

"""
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