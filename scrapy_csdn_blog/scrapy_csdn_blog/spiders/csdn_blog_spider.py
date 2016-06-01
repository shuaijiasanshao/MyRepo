# coding:utf-8
import scrapy
from scrapy.selector import Selector
from scrapy.http import Request
from scrapy_csdn_blog.items import BlogInfo

class CSDNBlogSpider(scrapy.spiders.Spider):
    
    name = "csdn_blog_spider"
    allowed_domains = ["blog.csdn.net"]
    # 博客的入口
    start_urls = ['http://blog.csdn.net/shuaijiasanshao/']

    def parse(self, response):
        # 爬取该页所有的博客title和url
        for div in response.xpath('//div[@class="article_title"]'):
            blog = BlogInfo()
            title = str(div.xpath('h1/span/a/text()').extract()[0]).strip()
            url = 'http://blog.csdn.net' + str(div.xpath('h1/span/a/@href').extract()[0])
            blog['title'] = title
            blog['url'] = url
            yield blog

        # 获取下一页的url
        for item in response.xpath('//div[@class="pagelist"]/a').extract():
            if Selector(text=item).xpath('//a/text()').extract()[0] == '下一页':
                next_url = 'http://blog.csdn.net'
                next_url += Selector(text=item).xpath('//a/@href').extract()[0]
                yield Request(next_url, callback=self.parse)
                