import scrapy
from scrapy.loader import ItemLoader
from scrapy_test.items import ScrapyTestItem


class QuotesToScrapeSpider(scrapy.Spider):
    name = 'quotesbot'
    allowed_domains = ['quotes.toscrape.com']
    start_urls = ['https://quotes.toscrape.com/']

    def parse(self, response):
        for section in response.xpath("//div[@class='quote']"):
            loader = ItemLoader(item=ScrapyTestItem(),
                                selector=section, response=response)
            loader.add_xpath('text', ".//span[@class='text']/text()")
            loader.add_xpath('author', ".//small[@class='author']/text()")
            loader.add_xpath('tags', ".//a[@class='tag']/text()")
            # yield {
            #     'text': section.xpath(".//span[@class='text']/text()").get(),
            #     'author': section.xpath(".//small[@class='author']/text()").get(),
            #     'tags': section.xpath(".//a[@class='tag']/text()").getall()
            # }
            yield loader.load_item()

        try:
            next_page_url = response.xpath("//li[@class='next']/a/@href").get()
            if next_page_url is not None:
                next_url = response.urljoin(next_page_url)
                yield scrapy.Request(url=next_url, callback=self.parse)
        except:
            print("Last page")
