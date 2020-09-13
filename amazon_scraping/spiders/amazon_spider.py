# -*- coding: utf-8 -*-
import scrapy
import xlwt
from ..items import AmazonScrapingItem


class AmazonSpiderSpider(scrapy.Spider):
    name = 'amazon_spider'
    search_string = "iphone"
    start_urls = [
        'https://www.amazon.com.br/s?k={}'.format(search_string)
    ]

    def parse(self, response):
        product_div = response.css('div .s-asin .sg-col-inner')

        workbook = xlwt.Workbook()
        sheet = workbook.add_sheet('Produtos')

        sheet.write(0,0,u"Nome")
        sheet.write(0,1,u"Preço")

        for index, product in enumerate(product_div):
            product_name = product.css(
                    '.a-color-base.a-text-normal::text').extract()
            product_price = product.css(
                    '.a-offscreen:nth-child(1)::text').extract()
            
            sheet.write(index + 1, 0, product_name)
            sheet.write(index + 1, 1, product_price)

            yield {
                'Nome': product_name,
                'Preço': product_price
            }
        
        workbook.save('produtos.xls')
