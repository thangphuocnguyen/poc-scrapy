"""Spider for Ghost Blog."""
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from scrapydemo.items import GhostLinkItem, GhostPostItem


class GhostSpider(CrawlSpider):
    """GhostSpider."""

    name = 'ghost_spider'
    allowed_domains = ['192.168.99.100', 'localhost:2368']

    session_id = -1  # Default session_id

    start_urls = [
        'http://192.168.99.100/',
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
        #

        item = GhostLinkItem()
        self.log('KIND -----> Ghost link!\n===========================')

        item['session_id'] = self.session_id
        self.log('session_id: %s' % item['session_id'])

        item['current_url'] = response.url
        self.log('current_url: %s' % item['current_url'])

        item['title'] = response.xpath('//title/text()').extract()
        self.log('title: %s' % item['title'])

        item['depth'] = response.meta['depth']
        self.log('depth: %s' % item['depth'])

        # response.request.headers.get('Referer', None) come from
        # the RefererMiddleware which is defaulted by SPIDER_MIDDLEWARES_BASE
        item['referring_url'] = response.request.headers.get('Referer', None) \
                                        .decode('utf-8')
        self.log('referring_url: %s' % item['referring_url'])

        yield item

    def parse_author_posts(self, response):
        """Parse post from author's page."""
        #

        for sel in response.xpath("//article[@class='post']"):

            post_item = GhostPostItem()
            self.log('KIND -----> Ghost post!\n===========================')

            post_item['title'] = sel.xpath('header/h2/a/text()') \
                                    .extract_first()
            self.log('title: %s' % post_item['title'])

            post_item['link'] = sel.xpath('header/h2/a/@href').extract_first()
            self.log('link: %s' % post_item['link'])

            post_item['desc'] = sel.xpath('section/p/text()').extract_first()
            self.log('desc: %s' % post_item['desc'])

            post_item['author'] = sel.xpath('footer/a/text()').extract_first()
            self.log('author: %s' % post_item['author'])

            yield post_item

        ghost_link_item = self.parse_item(response)
        yield ghost_link_item
