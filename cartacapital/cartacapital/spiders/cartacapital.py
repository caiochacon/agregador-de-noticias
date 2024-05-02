# -*- coding: utf-8 -*-
import scrapy
from cartacapital.items import CartacapitalItem

class SearchSpider(scrapy.Spider):
    name = 'cartacapital'
    allowed_domains = ['https://www.cartacapital.com.br/', 
                        'https://www.cartacapital.com.br/mais-recentes/']
    page_counter = 0
    max_pages = 10

    start_urls = [f'https://www.cartacapital.com.br/mais-recentes/'] 

    def parse(self, response):
      
      self.page_counter += 1

      link = response.css(".l-list__item")
      for item in link:
        yield from self.parse_article(item)

    #   next_page = response.css(".c-pagination__item+ .c-pagination__arrow a::attr(href)").get() #all()[:-2]
    #   if next_page is not None and self.page_counter < self.max_pages:
    #       yield response.follow(next_page, self.parse)
   

    def parse_article(self, content):

      title = content.css(".l-list__text h2").get()
      text = content.css(".l-list__text p").get()
      image = content.css(".l-list__image img").get()
      publication_date = content.css(".l-list__text span").get()
      link = content.css("a::attr(href)").get()
      
      # category = content.css(".feed-post-metadata-section::text").get()
      
      article = CartacapitalItem(title=title, publication_date=publication_date, 
                                text=text, link=link, image=image)
      yield article