import scrapy


class CunytestSpider(scrapy.Spider):
    name = "cunyTest"
    allowed_domains = ["pub.brooklyn.edu"]
    start_urls = ["https://pub.brooklyn.edu//DegreeMaps/stdnt_degree_maps_list.jsp"]

    def parse(self, response):
        self.log('Visiting: %s' % response.url)
        titles = response.css('a[href^="javascript:viewMap"]::text').getall()

        for title in titles:
            title = title.strip()
            yield {'title': title}

class cunyPdfSpider(scrapy.Spider):
    name = "cunyPdf"
    allowed_domains = ["pub.brooklyn.edu"]
    start_urls = ["https://pub.brooklyn.edu//DegreeMaps/stdn_view_degree_map.jsp"]

    def parse(self, response):
        self.log('visiting: %s' % response.url)
        links = response.css('a[href^=]::attr(href)').getall()

        for link in links:
            link = link.strip()
            yield {'found link': link}


