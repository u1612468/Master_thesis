import csv
import datetime
import pymysql

class ZlzpPipeline:
    def __init__(self, host, port, user, password, database):
        filename = 'job.csv'
        now = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        filename_with_timestamp = f"{filename[:-4]}_{now}{filename[-4:]}"
        self.f = open(filename_with_timestamp, 'w', encoding='utf-8', newline='')
        self.file_name = ['name','salary','company','adress','experience','eduBack','companyType','scale','info']
        self.writer = csv.DictWriter(self.f, fieldnames=self.file_name)
        self.writer.writeheader()
        self.host = host
        self.port = port
        self.user = user
        self.password = password
        self.database = database

    @classmethod
    def from_crawler(cls, crawler):
        return cls(
            host=crawler.settings.get('MYSQL_HOST'),
            port=crawler.settings.get('MYSQL_PORT'),
            user=crawler.settings.get('MYSQL_USER'),
            password=crawler.settings.get('MYSQL_PASSWORD'),
            database=crawler.settings.get('MYSQL_DATABASE')
        )

    def open_spider(self, spider):
        self.connection = pymysql.connect(
            host=self.host,
            port=self.port,
            user=self.user,
            password=self.password,
            database=self.database,
            charset='utf8mb4'
        )
        self.cursor = self.connection.cursor()

    def close_spider(self, spider):
        self.connection.commit()
        self.cursor.close()
        self.connection.close()
        self.f.close()


    def process_item(self, item, spider):
        self.writer.writerow(dict(item))
        sql = '''
            INSERT INTO job_internet (name, salary, company, address, experience, edu_back, company_type, scale, info)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
        '''
        values = (
            item['name'],
            item['salary'],
            item['company'],
            item['adress'],
            item['experience'],
            item['eduBack'],
            item['companyType'],
            item['scale'],
            ', '.join(item['info'])
        )
        self.cursor.execute(sql, values)
        return item
