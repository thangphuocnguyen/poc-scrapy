"""Spider for Ghost Blog."""
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from scrapydemo.items import GhostLinkItem, GhostPostItem


class GhostSpider(CrawlSpider):
    """GhostSpider."""

    name = 'ghost_spider'
    allowed_domains = ['192.168.99.101', 'localhost:2368']

    session_id = -1  # Default session_id

    start_urls = [
        'http://192.168.99.101/',
    ]

    rules = (

        # Parse author home page
        Rule(LinkExtractor(
             allow=r'\/author\/',
             ),
             callback='parse_author_posts',
             follow=True),

        Rule(LinkExtractor(allow=()),
             callback='parse_item',
             follow=True),
    )

    # receive session_id arguments in constructors, default = -1
    # specs session_id in command line by using -a session_id=<id>
    # ex: $ scrapy crawl ghost_spider -a session_id=1
    def __init__(self, session_id=-1, *args, **kwargs):
        """init."""
        super(GhostSpider, self).__init__(*args, **kwargs)
        self.session_id = session_id

    def parse_item(self, response):
        """Parse item."""
        print('hello--------------------')
        item = GhostLinkItem()

        item['session_id'] = self.session_id
        item['current_url'] = response.url
        item['title'] = response.xpath('//title/text()').extract()

        item['depth'] = response.meta['depth']

        # response.request.headers.get('Referer', None) come from
        # the RefererMiddleware which is defaulted by SPIDER_MIDDLEWARES_BASE
        item['referring_url'] = response.request.headers.get('Referer', None) \
                                        .decode('utf-8')

        yield item

    def parse_author_posts(self, response):
        """Parse post from author's page."""
        #
        print('res+++++++++++++++++++++++')
        for sel in response.xpath("//article[@class='post']"):

            post_item = GhostPostItem()
            post_item['title'] = sel.xpath('header/h2/a/text()').extract_first()
            post_item['link'] = sel.xpath('header/h2/a/@href').extract_first()
            post_item['desc'] = sel.xpath('section/p/text()').extract_first()
            post_item['author'] = sel.xpath('footer/a/text()').extract_first()
            # post_item['author'] = sel.xpath('section/p/text()').extract_first()
            yield post_item

        ghost_link_item = self.parse_item(response)
        yield ghost_link_item
