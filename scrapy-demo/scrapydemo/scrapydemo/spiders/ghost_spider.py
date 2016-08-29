
from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors.lxmlhtml import LxmlLinkExtractor
from scrapydemo.items import GhostLinkItem

class GhostSpider(CrawlSpider):

    name = 'ghost_spider'
    allowed_domains = ["192.168.99.101"]

    start_urls = [
        "http://192.168.99.101/",
    ]

    rules = (Rule(LxmlLinkExtractor(allow=()), callback='parse_obj', follow=True),)

    def parse_obj(self,response):

        item = GhostLinkItem()
        item['link'] = []
        for link in LxmlLinkExtractor(allow=(), deny=self.allowed_domains).extract_links(response):
            item['link'].append(link.url)
        yield item
