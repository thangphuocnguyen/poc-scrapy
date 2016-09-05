# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html


# class ScrapydemoPipeline(object):
#     def process_item(self, item, spider):
#         return item

class DemoPipeline(object):
    """docstring for DemoPipeline."""

    def process_item(self, item, spider):
        """."""
        print('type:', type(item))

        # import pdb
        # pdb.set_trace()

        try:
            if(item['link']):
                print('This is a post!\n**********************************\n',
                      item['link'])

        except KeyError:
            pass

        return item
