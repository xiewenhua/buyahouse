# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


class SzHouseErPipeline:
    def process_item(self, item, spider):
        print(111)
        return item


class SzHousePipeline:
    def process_item(self, item, spider):
        print(2222)
        return item