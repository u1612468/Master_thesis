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
    #cities = ['530', '538', '763', '765','653']
    cities = ['530']
    page_count = 34

    def start_requests(self):
        self.keyword_index = 0
        self.current_keyword = self.keywords[self.keyword_index]
        self.page_index = 1
        self.city_index = 0
        self.current_city = self.cities[self.city_index]
        url = f'https://sou.zhaopin.com/?jl={self.current_city}&kw={self.current_keyword}&p={self.page_index}'
        yield scrapy.Request(url=url, callback=self.parse, meta={'city': self.current_city, 'keyword': self.current_keyword, 'page': self.page_index})

    def parse(self, response):
        jobList = response.xpath('//div[@class="positionlist"]/div/a')
        if response.xpath('//div[@class="page-empty"]'):
            # If page-empty class exists, stop searching for the current keyword
            self.page_index = 1
            self.keyword_index += 1
            if self.keyword_index < len(self.keywords):
                self.current_keyword = self.keywords[self.keyword_index]
                url = f'https://sou.zhaopin.com/?jl={self.current_city}&kw={self.current_keyword}&p={self.page_index}'
                yield scrapy.Request(url=url, callback=self.parse, meta={'city': self.current_city, 'keyword': self.current_keyword, 'page': self.page_index})
            else:
                self.keyword_index = 0
                self.page_index = 1
                self.city_index += 1
                if self.city_index < len(self.cities):
                    self.current_city = self.cities[self.city_index]
                    self.current_keyword = self.keywords[self.keyword_index]
                    url = f'https://sou.zhaopin.com/?jl={self.current_city}&kw={self.current_keyword}&p={self.page_index}'
                    yield scrapy.Request(url=url, callback=self.parse, meta={'city': self.current_city, 'keyword': self.current_keyword, 'page': self.page_index})
        else:
            city = response.meta['city']
            page = response.meta['page'] + 1
            if page <= self.page_count:
                url = f'https://sou.zhaopin.com/?jl={city}&kw={self.current_keyword}&p={page}'
                yield scrapy.Request(url=url, callback=self.parse, meta={'city': city, 'keyword': self.current_keyword, 'page': page})
            else:
                self.page_index = 1
                self.keyword_index += 1
                if self.keyword_index < len(self.keywords):
                    self.current_keyword = self.keywords[self.keyword_index]
                    url = f'https://sou.zhaopin.com/?jl={self.current_city}&kw={self.current_keyword}&p={self.page_index}'
                    yield scrapy.Request(url=url, callback=self.parse, meta={'city': self.current_city, 'keyword': self.current_keyword, 'page': self.page_index})
                else:
                    self.keyword_index = 0
                    self.page_index = 1
                    self.city_index += 1
                    if self.city_index < len(self.cities):
                        self.current_city = self.cities[self.city_index]
                    self.current_keyword = self.keywords[self.keyword_index]
                    url = f'https://sou.zhaopin.com/?jl={self.current_city}&kw={self.current_keyword}&p={self.page_index}'
                    yield scrapy.Request(url=url, callback=self.parse)

            for job in jobList:
                    job_url = job.xpath('@href').get()
                    name = job.xpath("./div[1]/div[1]/span/@title").get()
                    info = job.xpath("./div[3]/div[1]//text()").extract()
                    salary = job.xpath("./div[2]/div[1]/p/text()").extract_first()
                    if salary:
                        salary = salary.strip()
                    company = job.xpath("./div[1]/div[2]/span[1]/text()").extract_first()
                    if company:
                        company = company.strip()
                    address = job.xpath("./div[2]/div[1]/ul/li[1]/text()").extract_first()
                    if address:
                        address = address.strip()
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
                    item = ZlzpItem(name=name, salary=salary, company=company, address=address, experience=experience, eduBack=eduBack, companyType=companyType, scale=scale, info=info, job_url=job_url)
                    yield item
