from scrapy.selector import Selector
from scrapy import Spider
from scrapy.contrib.spiders import CrawlSpider,Rule
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
from Ch3.wikiSpider.wikiSpider.items import Article

class ArticleSpider(CrawlSpider):
    name="article"
    allowed_domain=["en.wikipedia.org"]
    start_url=["https://en.wikipedia.org/wiki/Main_Page"]
    rules=[Rule(SgmlLinkExtractor(allow=('(/wiki/)((?!:).)*$'),),
                callback="parse",follow=True)]
    def parse(self, response):
         item=Article()
         title=response.xpath('//h1/text()')[0].extrcat()
         print("Title is:"+title)
         item['title']=title
         return item