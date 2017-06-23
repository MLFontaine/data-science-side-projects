import scrapy

class FunbagSpider(scrapy.Spider):
    name = 'funbag_urls'
    start_urls = ['http://deadspin.com/tag/funbag']

    def parse(self, response):
        for entry in response.css('h1.entry-title'):
            yield {
                'url': entry.css('a::attr(href)').extract_first(),
            }

        next_page = response.css('div.load-more__button a::attr(href)').extract_first()
        if next_page is not None:
            next_page_url = 'http://deadspin.com/tag/funbag' + next_page
            yield scrapy.Request(next_page_url)
            