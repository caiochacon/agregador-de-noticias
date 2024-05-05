from .scrapy_all.spiders.g1 import G1Spider as g1
from .scrapy_all.spiders.folha import FolhaSpider as folha
from .scrapy_all.spiders.cartacapital import CartacapitalSpider as cartacapital

from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings

# print("TESTES")

class ScrapyRunner:
  @staticmethod
  def run():
    # Obter as configurações do projeto Scrapy
    settings = get_project_settings()
    # Criar um processo com as configurações
    process = CrawlerProcess(settings)
    # Adicionar as spiders ao processo
    process.crawl(folha)
    process.crawl(g1)
    process.crawl(cartacapital)
    process.start()
