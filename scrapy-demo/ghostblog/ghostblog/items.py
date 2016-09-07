"""Scrapy item's specs."""
# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

from scrapy.item import Item, Field


class GhostPostItem(Item):
    """Post Item."""

    title = Field()
    author = Field()
    content = Field()
    post_date = Field()

    # Housekeeping fields
    url = Field()
    project = Field()
    spider = Field()
    server = Field()
    crawl_date = Field()
