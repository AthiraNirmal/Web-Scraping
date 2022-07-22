# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

# import scrapy


# class StackItem(scrapy.Item):
#     # define the fields for your item here like:
#     # name = scrapy.Field()
#     pass


from scrapy.item import Item, Field


class StackItem(Item):
    Title = Field()
    views = Field()
