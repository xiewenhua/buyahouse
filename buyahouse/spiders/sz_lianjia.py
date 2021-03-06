import scrapy

class szLianjiaErSpider(scrapy.Spider):
    name = "sz_lianjia"
    custom_settings = {
        'ITEM_PIPELINES': {
            'buyahouse.pipelines.SzHousePipeline': 200
        }
    }
    def start_requests(self):
        urls = [
            "https://sz.lianjia.com/ershoufang/",
            "https://sz.lianjia.com/ershoufang/pg/2"
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        page = response.url.split("/")[-2]
        print(page)
        print(response.body)