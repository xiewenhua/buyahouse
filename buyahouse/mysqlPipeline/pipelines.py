from .sql import lianjiaSql
from buyahouse.items import BuyahouseItem

class SzLianjiaErPipeline(object):
    def process_item(self, item, spider):
        if isinstance(item, BuyahouseItem):
            print('处理深圳二手房')
        # elif isinstance(item, SzLianjiaItem):
        #     print('处理深圳新房')