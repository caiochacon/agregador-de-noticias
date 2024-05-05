import scrapy
from ..items import ScrapyAllItem, MAX_PAGES


class FolhaSpider(scrapy.Spider):
    name = "folha"
    allowed_domains = ['search.folha.uol.com.br', 
                        'www1.folha.uol.com.br']
    page_counter = 0
    max_pages = MAX_PAGES

    start_urls = [f'http://search.folha.uol.com.br/?q=*'] 

    def parse(self, response):
      
      self.page_counter += 1

      link = response.css(".c-headline__content")
      for item in link:
        yield from self.parse_article(item, response)

      next_page = response.css(".c-pagination__item+ .c-pagination__arrow a::attr(href)").get() #all()[:-2]
      if next_page is not None and int(self.page_counter) < int(self.max_pages):
          yield response.follow(next_page, self.parse)
   

    def parse_article(self, content, response):

      title = content.css(".c-headline__title::text").get()
      text = content.css('.c-headline__standfirst::text').get()
      image = response.css(".c-headline__image::attr(src)").get()
      # category = content.css('.c-search__result_h3::text').get()
      publication_date = content.css('.c-headline__dateline::text').get()
      link = content.css('.c-headline__content a::attr(href)').get()
      
      article = ScrapyAllItem(title=title, publication_date=publication_date, 
                                text=text, link=link, image=image)#, category=category)
      yield article
