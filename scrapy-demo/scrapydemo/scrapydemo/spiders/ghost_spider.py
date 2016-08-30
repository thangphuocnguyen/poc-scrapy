
from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from scrapydemo.items import GhostLinkItem


class GhostSpider(CrawlSpider):

    name = 'ghost_spider'
    allowed_domains = ['192.168.99.101']

    session_id = -1

    start_urls = [
        'http://192.168.99.101/',
    ]

    rules = (Rule(LinkExtractor(allow=()),
             callback='parse_item',
             follow=True),)

    # receive session_id arguments in constructors, default = -1
    # specs session_id in command line by using -a session_id=<id>
    # ex: $ scrapy crawl ghost_spider -a session_id=1
    def __init__(self, session_id=-1, *args, **kwargs):
        super(GhostSpider, self).__init__(*args, **kwargs)
        self.session_id = session_id

    def parse_item(self, response):

        item = GhostLinkItem()

        item['session_id'] = self.session_id
        item['current_url'] = response.url
        item['title'] = response.xpath('//title/text()').extract()

        item['depth'] = response.meta['depth']

        # response.request.headers.get('Referer', None) come from
        # the RefererMiddleware which is defaulted by SPIDER_MIDDLEWARES_BASE
        item['referring_url'] = response.request.headers.get('Referer', None) \
                                        .decode('utf-8')

        return item
