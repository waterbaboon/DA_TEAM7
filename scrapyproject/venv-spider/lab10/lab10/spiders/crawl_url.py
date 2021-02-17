from abc import ABC

import scrapy


class URLSpider(scrapy.Spider, ABC):
    name = 'url_spider'
#    allowed_domains = ['www.ite.edu.sg']
    start_urls = ['http://www.twitter.com']

    def parse(self, response, **kwargs):
        css_selector = 'img'
        for x in response.css(css_selector):
            news = '@src'
            yield {
                'Image Link': x.xpath(news).extract_first(),
            }
            page_selector = '.next a ::attr(href)'
            next_page = response.css(page_selector).extract_first()
            if next_page:
                yield scrapy.Request(response.urljoin(next_page), callback=self.parse)
