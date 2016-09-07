# -*- coding: utf-8 -*-

import datetime
# import urlparse
import socket

from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from scrapy.loader import ItemLoader
# from scrapy.loader.processors import MapCompose, Join
from ghostblog.items import GhostPostItem


class GhostPostSpider(CrawlSpider):

    name = 'ghost_post_spider'
    allowed_domains = ['192.168.99.100']
    start_urls = ['http://192.168.99.100/']

    rules = (
        Rule(
            LinkExtractor(
                restrict_xpaths="//a[contains(@class, 'older-posts')]"
            )
        ),
        Rule(
            LinkExtractor(
                restrict_xpaths="//article[contains(@class, 'post')]" +
                "/header/h2/a"
            ),
            callback='parse_item',
        ),
    )

    def parse_item(self, response):

        print('-------', response.url, '-------')

        """ This function parses a post page.

        # @url http://192.168.99.101/demo-a-post/
        # @returns items 1
        # @scrapes title price description address image_urls
        # @scrapes url project spider server date
        """

        # Create the loader using the response
        l = ItemLoader(item=GhostPostItem(), response=response)

        # Load fields using XPath expressions
        l.add_xpath('title',
                    "//*[contains(@class,'post-title')][1]/text()",
                    # MapCompose(unicode.strip, unicode.title)
                    )

        l.add_xpath('author',
                    "//footer[@class='post-footer']/" +
                    "section[@class='author']/h4/a/text()",
                    # MapCompose(unicode.strip)
                    )

        l.add_xpath('content',
                    "//section[@class='post-content'][1]",
                    # MapCompose(unicode.strip), Join()
                    )

        l.add_xpath('post_date',
                    "//section/time[contains(@class,'post-date')]/@datetime",
                    # MapCompose(unicode.strip)
                    )

        # Housekeeping fields
        l.add_value('url', response.url)
        l.add_value('project', self.settings.get('BOT_NAME'))
        l.add_value('spider', self.name)
        l.add_value('server', socket.gethostname())
        l.add_value('crawl_date', datetime.datetime.now())

        return l.load_item()
