import scrapy
from target.items import TargetItem


class TargetSpider(scrapy.Spider):
    name = 'target'
    allowed_domains = ['target.com']

    def start_requests(self):
        link = 'https://www.target.com/p/tracfone-prepaid-apple-iphone-se-2nd-gen-64gb-black/-/A-82040163#lnk=sametab'
        request = scrapy.Request(url = link, callback = self.parse)
        #request.meta['proxy'] = ''
        yield request

    def parse(self, response):
        item = TargetItem()

        item['title'] = response.xpath('//*[@id="pageBodyContainer"]/div[1]/div[1]/h1/span/text()').get()
        #item['price'] = 
        images = response.xpath('//@src').extract()
        item['images'] = [image for image in images if (image.endswith('pjpeg') and 'wid=800' in image)]
        item['description'] = response.xpath('//*[@id="specAndDescript"]/div[1]/div[2]/div//text()').get()
        item['highlights'] =  response.xpath('//*[@id="tabContent-tab-Details"]/div/div/div/div[1]/div/div/ul//text()').extract()
        # item['last_question'] = 
        # item['last_answer'] = 
        yield item