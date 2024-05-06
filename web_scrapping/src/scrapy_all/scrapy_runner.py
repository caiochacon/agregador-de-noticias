from .spiders.g1 import G1Spider as g1
from .spiders.folha import FolhaSpider as folha
from .spiders.cartacapital import CartacapitalSpider as cartacapital
from scrapy.spiders import Spider
from scrapy.spiders import CrawlSpider
from .spiders import settings as my_settings

from scrapy.settings import Settings
from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings



class ScrapyRunner:
  @staticmethod
  def run():
    # Obter as configurações do projeto Scrapy
    crawler_settings = Settings()
    crawler_settings.setmodule(my_settings)
    process = CrawlerProcess(settings=crawler_settings)
    # Adicionar as spiders ao processo
    process.crawl(folha)
    process.crawl(g1)
    process.crawl(cartacapital)
    process.start()
    
if __name__ == '__main__':
  ScrapyRunner.run()

# from .spiders.g1 import G1Spider as g1
# from .spiders.folha import FolhaSpider as folha
# from .spiders.cartacapital import CartacapitalSpider as cartacapital

# from scrapy.crawler import CrawlerProcess
# from scrapy.utils.project import get_project_settings

# class ScrapyRunner:
#   @staticmethod
#   def run():
#     # Obter as configurações do projeto Scrapy
#     settings = get_project_settings()
#     # Criar um processo com as configurações
#     process = CrawlerProcess(settings)
#     # Adicionar as spiders ao processo
#     process.crawl(folha)
#     process.crawl(g1)
#     process.crawl(cartacapital)
#     process.start()