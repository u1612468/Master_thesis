BOT_NAME = 'zlzp'

SPIDER_MODULES = ['zlzp.spiders']
NEWSPIDER_MODULE = 'zlzp.spiders'
LOG_LEVEL = 'WARNING'

ROBOTSTXT_OBEY = False


DEFAULT_REQUEST_HEADERS = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.106 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Accept-Language': 'en',
}

DOWNLOADER_MIDDLEWARES = {
    'zlzp.middlewares.ZlzpDownloaderMiddleware': 543,
}

ITEM_PIPELINES = {
    'zlzp.pipelines.ZlzpPipeline': 300,
}


MYSQL_HOST = 'localhost'
MYSQL_PORT = 3306
MYSQL_USER = 'root'
MYSQL_PASSWORD = '19980721'
MYSQL_DATABASE = 'internet'