from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from selenium import webdriver
from scrapy.http import HtmlResponse

class ZlzpDownloaderMiddleware:
    def __init__(self):
        self.driver = webdriver.Chrome()
    def process_request(self, request, spider):
        self.driver.get(request.url)
        time.sleep(3)
        WebDriverWait(self.driver, 1000).until(
            EC.url_contains(request.url)
        )
        time.sleep(6)
        return HtmlResponse(url=self.driver.current_url, body=self.driver.page_source, encoding="utf-8",
                            request=request)