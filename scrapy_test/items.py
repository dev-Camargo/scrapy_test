import scrapy
from scrapy.loader.processors import MapCompose, TakeFirst, Join


def remove_blank_space(ch):
    return ch.strip()


def process_special_characters(ch):
    # Used Unicode Converter
    return ch.replace(u"\u201c", '').replace(u"\u201d", '').replace(u"\u2014", '-')


class ScrapyTestItem(scrapy.Item):
    text = scrapy.Field(input_processor=MapCompose(remove_blank_space, process_special_characters),
                        output_processor=TakeFirst()
                        )
    author = scrapy.Field(output_processor=TakeFirst())
    tags = scrapy.Field(output_processor=Join(','))
    pass
