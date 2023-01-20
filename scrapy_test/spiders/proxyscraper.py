import scrapy


class ProxyScraperSpider(scrapy.Spider):
    name = 'proxyscraper'
    allowed_domains = ['us-proxy.org']
    start_urls = ['https://us-proxy.org/']

    def parse(self, response):
        for linha in response.xpath("//table[@class='table table-striped table-bordered']//tr"):
            yield {
                'ip_address': linha.xpath("./td[1]/text()").get(),
                'port': linha.xpath("./td[2]/text()").get(),
                'code': linha.xpath("./td[3]/text()").get(),
                'country': linha.xpath("./td[4]/text()").get(),
                'anonymity': linha.xpath("./td[5]/text()").get(),
                'google': linha.xpath("./td[6]/text()").get(),
                'https': linha.xpath("./td[7]/text()").get(),
                'last_checked': linha.xpath("./td[8]/text()").get()
            }
