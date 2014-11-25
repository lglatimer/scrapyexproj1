import scrapy

from Demo_proj1.items import DemoProj1Item

class DemoProj1Spider(scrapy.Spider):
	name = "Tutorial"
	allowed_domains =["punchng.com"]
	start_urls = ["http://www.punchng.com"]

	def parse(self, response):
		for url in response.xpath('//*'):
			item = DemoProj1Item()
			item['link'] = url.xpath('a/@href').extract()
			yield item