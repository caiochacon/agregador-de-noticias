# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
from datetime import datetime, timedelta

class ScrapyG1Pipeline:
    def process_item(self, item, spider):
      
        item['source'] = "G1"
        
        current_time = datetime.now()

        if 'minuto' in item['publication_date']:
            minutes = int(item['publication_date'].split()[1])
            posted_time = current_time - timedelta(minutes=minutes)
            item['publication_date'] = posted_time
        elif 'hora' in item['publication_date']:
            hours = int(item['publication_date'].split()[1])
            posted_time = current_time - timedelta(hours=hours)
            item['publication_date'] = posted_time
        elif 'ontem' in item['publication_date']:
            posted_time = current_time - timedelta(days=1)
            item['publication_date'] = posted_time
        elif 'dia' in item['publication_date']:
            days = int(item['publication_date'].split()[1])
            posted_time = current_time - timedelta(days=days)
            item['publication_date'] = posted_time
        elif 'semana' in item['publication_date']:
            weeks = int(item['publication_date'].split()[1])
            posted_time = current_time - timedelta(weeks=weeks)
            item['publication_date'] = posted_time
        elif 'mês' in item['publication_date']:
            months = int(item['publication_date'].split()[1])
            # Aproximação de 30 dias por mês
            posted_time = current_time - timedelta(days=months * 30)
            item['publication_date'] = posted_time
        

        
        return item
