import scrapy
from buyahouse.items import BuyahouseItem


class szLianjiaErSpider(scrapy.Spider):
    name = "sz"
    # custom_settings = {
    #     'ITEM_PIPELINES': {
    #         'buyahouse.pipelines.SzHouseErPipeline': 100
    #     }
    # }

    def start_requests(self):
        urls = ["https://sz.lianjia.com/ershoufang/pg" +
                str(i) for i in range(1, 2)]
        # urls = [
        #     "https://sz.lianjia.com/ershoufang/",
        #     # "https://sz.lianjia.com/ershoufang/pg/2"
        # ]
        for url in urls:
            # print("============此处翻页=============")
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        """房屋列表页面"""
        # page = response.url.split("/")[-2]
        # print(page)
        # print(response.body)

        item = BuyahouseItem()
        houselinks = response.xpath(
            '//div[@class="title"]/a[@data-housecode]/@href').extract()
        # print("当前页面有效链接："+str(len(houselinks)))

        for houselink in houselinks:

            # print(houselink)
            yield scrapy.Request(url=houselink, callback=self.parse_content, meta={'key': item, 'houselink': houselink})

    def parse_content(self, response):
        """详情页面"""
        item = response.meta['key']
        item['url'] = response.meta['houselink']
        # print("writed: "+item['url'])
        item['title'] = response.xpath("//h1[@title]/@title").extract()
        # print(item['title'])
        item['price'] = response.xpath(
            "//span[@class='total']/text()").extract()
        item['price_per_square'] = response.xpath(
            "//span[@class='unitPriceValue']/text()").extract()
        item['community_name'] = response.xpath(
            '//div[@class="communityName"]/a[@target]/text()').extract()
        # 输出Bug
        item['area'] = response.xpath(
            '/html/body/div[5]/div[2]/div[5]/div[2]/span[2]/a/text()').extract()
        item['number'] = response.xpath(
            '//div[@class="houseRecord"]/span[2]/text()').extract()

        item['housing_type'] = response.xpath(
            '//*[@id="introduction"]/div/div/div[1]/div[2]/ul/li[1]/text()').extract()
        # print(item['housing_type'])
        item['construction_area'] = response.xpath(
            '//*[@id="introduction"]/div/div/div[1]/div[2]/ul/li[3]/text()').extract()
        item['inside_area'] = response.xpath(
            '//*[@id="introduction"]/div/div/div[1]/div[2]/ul/li[5]/text()').extract()
        item['unit_structure'] = response.xpath(
            '//*[@id="introduction"]/div/div/div[1]/div[2]/ul/li[4]/text()').extract()
        item['building_structure'] = response.xpath(
            '//*[@id="introduction"]/div/div/div[1]/div[2]/ul/li[6]/text()').extract()
        item['house_orientation'] = response.xpath(
            '//*[@id="introduction"]/div/div/div[1]/div[2]/ul/li[7]/text()').extract()
        item['building_structure'] = response.xpath(
            '//*[@id="introduction"]/div/div/div[1]/div[2]/ul/li[8]/text()').extract()
        item['renovation_condition'] = response.xpath(
            '//*[@id="introduction"]/div/div/div[1]/div[2]/ul/li[9]/text()').extract()
        item['staircase_ratio'] = response.xpath(
            '//*[@id="introduction"]/div/div/div[1]/div[2]/ul/li[10]/text()').extract()
        item['equipped_with_elevator'] = response.xpath(
            '//*[@id="introduction"]/div/div/div[1]/div[2]/ul/li[11]/text()').extract()

        item['listing_time'] = response.xpath(
            '//*[@id="introduction"]/div/div/div[2]/div[2]/ul/li[1]/span[2]/text()').extract()
        item['housing_society_code'] = response.xpath(
            '//*[@id="introduction"]/div/div/div[2]/div[2]/ul/li[2]/span[2]/text()').extract()
        item['last_transaction'] = response.xpath(
            '//*[@id="introduction"]/div/div/div[2]/div[2]/ul/li[3]/span[2]/text()').extract()
        item['usage_of_houses'] = response.xpath(
            '//*[@id="introduction"]/div/div/div[2]/div[2]/ul/li[4]/span[2]/text()').extract()
        item['housing_years'] = response.xpath(
            '//*[@id="introduction"]/div/div/div[2]/div[2]/ul/li[5]/span[2]/text()').extract()
        item['ownership'] = response.xpath(
            '//*[@id="introduction"]/div/div/div[2]/div[2]/ul/li[6]/span[2]/text()').extract()
        item['mortgage_information'] = response.xpath(
            '//*[@id="introduction"]/div/div/div[2]/div[2]/ul/li[7]/span[2]/text()').extract()[0].strip()
        item['room_spare_parts'] = response.xpath(
            '//*[@id="introduction"]/div/div/div[2]/div[2]/ul/li[8]/span[2]/text()').extract()

        # print(item)

        yield item
