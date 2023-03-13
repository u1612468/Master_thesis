# -*- coding: utf-8 -*-
import scrapy
from zlzp.ZlzpItem import ZlzpItem

count = 1
class ZlSpider(scrapy.Spider):
    name = 'zl'
    allowed_domains = ['zhaopin.com']
    keywords = ['Java开发','UI设计师','Web前端','PHP',
                'Python','Android','美工', '深度学习',
                '算法工程师','Hadoop','Node.js','数据开发',
                '数据分析师','数据架构','人工智能','区块链',
                "电气工程师","电子工程师","PLC测试工程师",
                "设备工程师","硬件工程师","结构工程师",
                "工艺工程师","产品经理","新媒体运营",
                "运营专员","淘宝运营","天猫运营","产品助理",
                "产品运营","淘宝客服","游戏运营","编辑",
                "投资经理","风控","催收","银行柜员",
                "银行销售","信审","信用卡","贷款",
                "金融产品","汽车金融","金融研究",
                "证券","交易员","投资经理","期货",
                "操盘手","基金","股票","投资顾问",
                "信托","典当","担保","信贷","权证",
                "财产保险","保险内勤","理赔","精算师",
                "保险销售","理财顾问","查勘定损","车险"]
    cities = ['530', '538', '763', '765','653']
    page_count = 34

    def start_requests(self):
        for keyword in self.keywords:
            for city in self.cities:
                for page in range(1, self.page_count + 1):
                    url = f'https://sou.zhaopin.com/?jl={city}&kw={keyword}&p={page}'
                    yield scrapy.Request(url=url, callback=self.parse, meta={'city': city, 'keyword': keyword, 'page': page})

    def parse(self, response):
        global count
        count += 1  # 每解析一次页面，让count+1，和baseurl构造下一页的url
        jobList = response.xpath('//div[@class="positionlist"]/div/a')

        for job in jobList:
            name = job.xpath("./div[1]/div[1]/span/@title").get()
            info = job.xpath("./div[3]/div[1]//text()").extract()
            salary = job.xpath("./div[2]/div[1]/p/text()").extract_first()
            if salary:
                salary = salary.strip()
            company = job.xpath("./div[1]/div[2]/span[1]/text()").extract_first()
            if company:
                company = company.strip()
            adress = job.xpath("./div[2]/div[1]/ul/li[1]/text()").extract_first()
            if adress:
                adress = adress.strip()
            experience = job.xpath("./div[2]/div[1]/ul/li[2]/text()").extract_first()
            if experience:
                experience = experience.strip()
            eduBack = job.xpath("./div[2]/div[1]/ul/li[3]/text()").extract_first()
            if eduBack:
                eduBack = eduBack.strip()
            companyType = job.xpath("./div[2]/div[2]/span[1]/text()").extract_first()
            if companyType:
                companyType = companyType.strip()
            scale = job.xpath("./div[2]/div[2]/span[2]/text()").extract_first()
            if scale:
                scale = scale.strip()
            item = ZlzpItem(name=name,salary=salary,company=company,adress=adress,experience=experience,eduBack=eduBack,companyType=companyType,scale=scale,info=info)
            yield item
