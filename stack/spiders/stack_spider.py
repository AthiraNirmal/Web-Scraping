from scrapy import Spider
from scrapy.selector import Selector

from stack.items import StackItem

#Crawling into StackOverFlow
#Retrieving Question and Number of views from StackOverFlow

class StackSpider(Spider):
    name = "stack"
    
    allowed_domains = ["stackoverflow.com"] 
    start_urls = [
        "http://stackoverflow.com/questions?pagesize=50&sort=newest",
    ]

    def parse(self, response):

        questions = response.xpath("//div[@class='s-post-summary js-post-summary']")

        for question in questions:
            item = StackItem()

            item_name = question.xpath(".//div[@class= 's-post-summary--content']//h3//a//text()").get()
            item['Title']=item_name
            # view_text= question.xpath(".//div//div//span[@class= 's-post-summary--stats-item-unit']//text()").get()
            view_number= question.xpath(".//div//div[3]//span[@class= 's-post-summary--stats-item-number']//text()").get()
            item['views']=view_number
            # if view_text is views:
            #     view_number= question.xpath(".//div//div//span[@class= 's-post-summary--stats-item-number']//text()").get()

            # item['title'] = question.xpath(
            #     'a[@class="question-hyperlink"]/text()').extract()[0]
            # item['url'] = question.xpath(
            #     'a[@class="question-hyperlink"]/@href').extract()[0]
            # yield {
            #     'TOPIC':item_name,
            #     'VIEWS':view_number,
            # }
            yield item
