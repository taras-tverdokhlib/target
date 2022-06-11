# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

from pandas import describe_option
import scrapy


class TargetItem(scrapy.Item):
    # define the fields for your item here like:
    title = scrapy.Field()
    price = scrapy.Field()
    images = scrapy.Field()
    description = scrapy.Field()
    highlights = scrapy.Field()
    last_question = scrapy.Field()
    last_answer = scrapy.Field()
    pass
