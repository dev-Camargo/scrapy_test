import scrapy


class QuotesToScrapeSpider(scrapy.Spider):
    name = 'quotesbot'
    allowed_domains = ['quotes.toscrape.com']
    start_urls = ['https://quotes.toscrape.com/']

    def parse(self, response):
        for section in response.xpath("//div[@class='quote']"):
            yield {
                'text': section.xpath(".//span[@class='text']/text()").get(),
                'author': section.xpath(".//small[@class='author']/text()").get(),
                'tags': section.xpath(".//a[@class='tag']/text()").getall()
            }
