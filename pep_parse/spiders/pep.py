import scrapy

from pep_parse.constaints import DOMAIN, URL
from pep_parse.items import PepParseItem


class PepSpider(scrapy.Spider):
    name = 'pep'
    allowed_domains = [DOMAIN]
    start_urls = [URL]

    def parse(self, response):
        all_peps = response.css(
            "a.pep.reference.internal::attr('href')"
        ).getall()
        for pep in all_peps:
            yield response.follow(pep, callback=self.parse_pep)

    def parse_pep(self, response):
        title = response.css('h1.page-title::text').get()
        number = int(title.split(" ")[1])
        name = title[(title.find(" – ") + 3):]
        status = response.css('dt:contains("Status") + dd abbr::text').get()
        data = {
            'number': number,
            'name': name,
            'status': status
        }
        yield PepParseItem(data)
