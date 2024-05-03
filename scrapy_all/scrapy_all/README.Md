Para rodar cada projeto individualmente, dentro da pasta agregador-de-noticias/scrappy_all, você pode utilizar o comando:

scrapy crawl folha.py
scrapy crawl cartacapital.py
scrapy crawl g1.py

Para rodar tudo, basta rodar no terminal python3 run_all_spiders.py

Para setar o número de páginas que o crawler vai retornar, basta ir no arquivo items.py e modificar o valor da variavel MAX_PAGES