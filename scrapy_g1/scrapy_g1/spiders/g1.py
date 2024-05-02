# -*- coding: utf-8 -*-
import scrapy
from scrapy_g1.items import ScrapyG1Item

class SearchSpider(scrapy.Spider):
    name = 'search'
    allowed_domains = ['https://g1.globo.com.br']
    page_counter = 0
    max_pages = 10000

    start_urls = [f'https://g1.globo.com/ultimas-noticias/']
    next_urls = [f'https://g1.globo.com/ultimas-noticias/index/feed/pagina-{num_page}.ghtml'
                 for num_page in range(2, max_pages+1)]
    start_urls.extend(next_urls)
    
    def parse(self, response):
      
      self.page_counter += 1

      link = response.css(".type-materia")
      for item in link:
        yield from self.parse_article(item, response)

    #   next_page = response.css("#feed-placeholder a::attr(href)").getall()[-1]
    #   print("#######################################################3")
    #   print("NEXT PAGE: ", next_page)
    #   if next_page is not None and self.page_counter < self.max_pages:
    #       self.start_urls.append(next_page)
    #       print("555555555555555555555555555555555555555555555553")
    #       print(self.start_urls)
    #       yield response.follow(next_page, self.parse)
   

    def parse_article(self, content, response):

      title = content.css(".gui-color-hover p::text").get()
      text = content.css(".feed-post-body-resumo p::text").get()
      image = response.css(".bstn-fd-picture-image::attr(src)").get()
      publication_date = content.css(".feed-post-datetime::text").get()
      category = content.css(".feed-post-metadata-section::text").get()
      link = content.css(".feed-media-wrapper a::attr(href)").get()
      
      article = ScrapyG1Item(title=title, publication_date=publication_date, 
                                text=text, link=link, image=image, category=category)
      yield article
