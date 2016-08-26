import scrapy

from scrapydemo.items import GhostPostItem


class GhostBlogSpider(scrapy.Spider):

    name = "ghost_blog_post"
    allowed_domains = ["192.168.99.101"]

    start_urls = [
        "http://192.168.99.101/",
    ]

    def parse(self, response):

        # Write the respone into html file
        filename = response.url.split("/")[-2] + '.html'

        # Join storage directory for exported file
        filename = 'item-storage/' + filename

        with open(filename, 'wb') as f:
            f.write(response.body)

        # Export post items
        for sel in response.xpath("//article"):

            post_item = GhostPostItem()
            post_item['title'] = sel.xpath('header/h2/a/text()').extract_first()
            post_item['link'] = sel.xpath('header/h2/a/@href').extract_first()
            post_item['desc'] = sel.xpath('section/p/text()').extract_first()
            yield post_item
