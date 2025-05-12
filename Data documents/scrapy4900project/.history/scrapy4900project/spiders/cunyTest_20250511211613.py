import scrapy


class CunytestSpider(scrapy.Spider):
    name = "cunyTest"
    allowed_domains = ["www.brooklyn.edu"]
    start_urls = ["https://www.brooklyn.edu/"]

    def parse(self, response):
        pass
