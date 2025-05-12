import scrapy


class CunytestSpider(scrapy.Spider):
    name = "cunyTest"
    allowed_domains = ["https://www.brooklyn.edu"]
    start_urls = ["https://pub.brooklyn.edu//DegreeMaps/stdnt_degree_maps_list.jsp"]

    def parse(self, response):
        self.log('Visiting: %s' % response.url)
        titles = response.css('td::text').getall()

        for title in titles:
            yield {'title': title}
