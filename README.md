# Web_Crawler
The code of Web_Crawler(using python) I learned for about one month.  
day01:  
    &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;01-第一个爬虫.py：爬取一个网页的源代码  
    &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;02-Request的使用.py：对请求头进行封装，伪装User-agent  
    &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;03-fake_useragent测试.py：Python库(fake-useragent),可以随机生成各种UserAgent  
    &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;04-get请求1.py：利用Request库的quote对中文字符进行编码  
    &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;05-get请求2.py：利用Request库的urlencode对中文字符进行编码  
    &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;06-贴吧案例.py：对百度贴吧任意网页源代码进行爬取  
    &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;07-post请求：发送post请求登录页面  

day02:  
    &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;08-ajax请求的使用.py：爬取豆瓣电影动态页面  
    &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;09-https请求.py：请求SSL证书验证，12306网站为例  
    &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;10-opener的使用.py：利用opener创建urlopen  
    &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;11-proxy的使用.py：设置代理proxy  
    &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;12-cookie的使用.py：登录成功后，引入Cookie访问页面，实时  
    &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;13-cookie的使用2.py：未在网页上登录，利用表单信息先登录再访问页面  
    &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;14-cookie的使用3.py：将cookie保存到文件中，然后从文件中加载出来  
    &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;15-URLError的使用.py：用try-except语句来包围并捕获相应的异常  
    &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;16-request的使用1.py：requests 库的基本用法  
    &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;17-request的使用2.py：requests 库的基本用法，登录页面  
    &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;18-request的使用3.py：requests 库的基本用法，proxy代理  
    &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;19-request的使用4.py：requests 库的基本用法，SSL证书问题  
    &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;20-request的使用5.py：requests 库的基本用法，session和cookie  

day03:  
    &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;21-re的使用.py：正则表达式进行字符串的匹配  
    &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;22-糗事百科案例.py：对糗事百科上的段子进行爬取  
    &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;23-beautifulsoup的使用.py：BeautifulSoup通过解析文档为用户提供需要抓取的数据  
    &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;24-xpath的使用.py：利用Xpath库爬取起点中文网小说名称和作者信息  
    &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;25-pyquery的使用.py：利用pyquery库对西刺代理网站的IP地址进行爬取  
    &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;26-json的使用.py：json模块提供了四个功能：dumps、dump、loads、load，用于字符串和python数据类型间进行转换  
    &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;27-jsonpath的使用.py：利用jsonpath库爬取拉勾网城市JSON文件，获取所有城市和代码  

day04:  
    &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;28-多线程的使用.py：应用多线程爬取糗事百科段子  
    &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;29-tesseractOCR的使用.py：tesseract是一个google支持的开源ocr项目，可以识别验证码  
    &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;YDMHTTPDemo3.py：云打码平台识别验证码的代码接口  
    &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;30-云打码登录.py：利用云打码平台对验证码进行识别输入，登录网站  
    &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;31-爬取图文并茂文章方法.py：对新闻网站这样的图文并茂的网站进行爬取，以中文新闻网为例  
    &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;32-selenium的使用.py：熟悉Web应用程序测试的工具Selenium，Selenium测试直接运行在浏览器中  

day05:  
    &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;movie1.py：利用 Xpath 爬取‘猫眼电影’的电影名称、电影类型、电影演员  
    &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;movie2.py：利用 PS4 爬取‘猫眼电影’的电影名称、电影类型、电影演员  
    &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;movie3.py：利用 re 正则表达式 爬取‘猫眼电影’的电影名称、电影类型、电影演员  
    &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;movie4.py：利用 pyquery 爬取‘猫眼电影’的电影名称、电影类型、电影演员  
 
day06:  
    &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;33-selenium的简单使用.py：ChromeDriver开启无头模式(不打开浏览器页面)  
    &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;34-斗鱼直播练习.py：爬取斗鱼直播平台的主播以及观众人数（热度）等基本信息  
    &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;35-selenium滚动条的使用.py：对滚动页面进行滚动条的使用  
    &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;36-图虫网爬取图片.py：对图虫网的图片进行爬取图片练习  
    &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;37-双色球数据下载.py：对彩票网站双色球下注数据进行爬取练习，并将数据存储到mysql数据库中,并且对数据进行更新  
    &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;38-爬虫新写法.py：将爬取流程抽取出类class  

demo1:  
    spiders:  
        &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;baidu.py：Scrapy框架的介绍和简单使用  
        &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;qidian.py：利用Scrapy框架爬取起点中文网的小说的名字和作者  
        &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;maoyan.py：利用Scrapy框架爬取猫眼电影名称和评分  

xiaoshuo:  
    spiders:  
        &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;zww.py：Scrapy框架对小说“武道巅峰"内容进行爬取  
        &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;zww2.py：Scrapy框架利用crawlSpider类对小说“龙王传说"内容进行爬取  

tupian:  
    spiders:  
        &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;zol.py：使用ImagesPipeline下载图片  
        &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;http_ua.py：重写middlewares.py文件，获取动态UA  
        &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;proxymiddlewares.py：scrapy中动态代理的使用演示  
        &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;baidu.py：演示模拟登录-Request、Response  

login:  
    spiders:  
        &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;login1.py：Scrapy登录方式1演示  
        &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;login2.py：Scrapy登录方式2演示  
        &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;login3.py：Scrapy登录方式3演示  

mongo_demo:  
    &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;mongo_demo.py：演示python和MongoDB交互，数据库连接以及操作数据  
    spiders:  
        &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;douban.py：爬取豆瓣电影Top250，将电影名和星级存入数据库中  

splash_demo:  
    &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;splash_demo.py：splash与requests结合  
    &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;splash_demo2.py：splash与requests结合，手写lua代码  
    &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;spiders:  
        &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;guazi.py：splash和Scrapy结合  
        &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;guazi2.py：splash和Scrapy结合，手写lua代码  

selenium_demo:  
    spiders:  
        &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;guazi.py：selenium和Scrapy结合，修改middlewares.py代码  

room:  
    &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;对链家网信息进行爬取，并将数据保存到数据库中(MongoDB和Mysql)  

duanzi:  
    spiders:  
        &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;scrapy_redis分布式爬虫框架的写法，让爬虫具有了分布式爬取的功能，TreeSoft数据库管理系统的使用  
    redis_mongoDB.py：从redis中取出数据库到MongoDB数据库中  

