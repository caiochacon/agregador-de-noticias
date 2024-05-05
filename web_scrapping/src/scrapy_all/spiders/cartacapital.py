import scrapy
from ..items import ScrapyAllItem, MAX_PAGES

class CartacapitalSpider(scrapy.Spider):
    name = "cartacapital"
    allowed_domains = ['https://www.cartacapital.com.br/', 
                        'https://www.cartacapital.com.br/mais-recentes/']
    page_counter = 0
    max_pages = MAX_PAGES

    start_urls = [f'https://www.cartacapital.com.br/mais-recentes/'] 
    
    next_urls = [f'https://www.cartacapital.com.br/mais-recentes/page/{num_page}/'
                for num_page in range(2, max_pages+1)]
    start_urls.extend(next_urls)

    def parse(self, response):
      
      self.page_counter += 1

      link = response.css(".l-list__item")
      for item in link:
        yield from self.parse_article(item)


    def parse_article(self, content):

      title = content.css(".l-list__text h2::text").get()
      text = content.css(".l-list__text p::text").get()
      image = content.css(".l-list__image img::attr(src)").get()
      publication_date = content.css(".l-list__text span").get()
      link = content.css("a::attr(href)").get()
      
      # category = content.css(".feed-post-metadata-section::text").get()
      
      article = ScrapyAllItem(title=title, publication_date=publication_date, 
                                text=text, link=link, image=image)
      yield article