"""Scrapy item's specs."""
# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class GhostLinkItem(scrapy.Item):
    """Link item."""

    # session_id: a unique session id for each scrapy run or harvest
    session_id = scrapy.Field()

    # depth: the depth of the current page with respect to the start url
    depth = scrapy.Field()

    # current_url: the url of the current page being processed
    current_url = scrapy.Field()

    # referring_url: the url of the site which was linked to the current page
    referring_url = scrapy.Field()

    title = scrapy.Field()

    # publish_date = scrapy.Field()


class GhostPostItem(scrapy.Item):
    """Post Item."""

    title = scrapy.Field()
    link = scrapy.Field()
    desc = scrapy.Field()
    author = scrapy.Field()
