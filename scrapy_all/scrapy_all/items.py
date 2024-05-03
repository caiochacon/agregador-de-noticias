# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy

MAX_PAGES = 100

class ScrapyAllItem(scrapy.Item):
    # define the fields for your item here like:
    title      = scrapy.Field()
    text       = scrapy.Field()
    publication_date = scrapy.Field()
    image     = scrapy.Field()
    link       = scrapy.Field()
    category   = scrapy.Field()
    source = scrapy.Field()