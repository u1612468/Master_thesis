import scrapy

class ZlzpItem(scrapy.Item):
    name = scrapy.Field()
    salary = scrapy.Field()
    company = scrapy.Field()
    adress = scrapy.Field()
    experience = scrapy.Field()
    eduBack = scrapy.Field()
    companyType = scrapy.Field()
    scale = scrapy.Field()
    info = scrapy.Field()