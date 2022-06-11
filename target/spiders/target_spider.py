import scrapy
from target.items import TargetItem


class TargetSpider(scrapy.Spider):
    name = 'target'
    allowed_domains = ['target.com']

    def start_requests(self):
        link = 'https://www.target.com/p/tracfone-prepaid-apple-iphone-se-2nd-gen-64gb-black/-/A-82040163#lnk=sametab'
        request = scrapy.Request(url = link, callback = self.parse)
        request.meta['proxy']: "http://lum-customer-monocl-zone-residential-country-us-session:ou0wrveuva1e@zproxy.lum-superproxy.io:22225"
        # meta={"proxy": "http://lum-customer-c_38e12ee8-zone-data_center:m2qurc5zg71t@zproxy.lum-superproxy.io:22225"})
        # meta={"proxy": "http://lum-customer-monocl-zone-residential-country-us-session-%s:ou0wrveuva1e@zproxy.lum-superproxy.io:22225"})
        yield request

    def parse(self, response):
        item = TargetItem()

        item['title'] = response.xpath('//*[@id="pageBodyContainer"]/div[1]/div[1]/h1/span/text()').get()
        item['price'] = response.xpath('/html/body/div[1]/div[2]/div/div[2]/div[1]/div[2]/div[2]/div/div[1]/div[1]/span').extract()
        item['images'] = response.xpath('//picture//@crc').extract()
        item['description'] = []
        descriptions = 
        item['highlights'] = []
        highlights = 
        # item['last_question'] = 
        # item['last_answer'] = 
        yield item