import subprocess
import sys

max_pages = sys.argv[1] if len(sys.argv) > 1 else 5

# Obter a lista de todos os spiders no projeto
spiders = subprocess.check_output(['scrapy', 'list']).decode().split()

# Rodar cada spider
for spider in spiders:
    print(f"Running spider: {spider}")
    subprocess.run(['scrapy', 'crawl', spider, "-a", f"max_pages={max_pages}"])
