import scrapy
from Demo_proj1.items import DemoProj1Item
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor


class DemoProj1Spider(scrapy.Spider):
	name = "Tutorial"
#	allowed_domains =["punchng.com"]
	start_urls = ["http://www.punchng.com"]
	rules = (Rule (SgmlLinkExtractor(allow=("", ),),
                callback="parse_items",  follow= True),
    )

	def parse_items(self, response):
		for url in response.xpath('//*'):
			item = DemoProj1Item()
			item['link'] = url.xpath('a/@href').extract()
			referring_url = response.request.headers.get('Referer', None)
			item['referring_url'] = referring_url
			item['depth'] = response.meta['depth']
			yield item