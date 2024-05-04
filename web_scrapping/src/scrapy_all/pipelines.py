# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import re
from datetime import datetime, timedelta
import pandas as pd
import os

class PandasCsvPipeline:
    def __init__(self):
        self.items = []

    def open_spider(self, spider):
        # Verifica se o arquivo já existe
        self.file_exists = os.path.exists('../../data/notices.csv')

    def close_spider(self, spider):
        # Cria um DataFrame a partir da lista de itens
        df = pd.DataFrame(self.items)

        if self.file_exists:
            # Se o arquivo já existir, carregue-o e adicione os novos dados
            existing_df = pd.read_csv('../../data/notices.csv', encoding='utf-8')
            df = pd.concat([existing_df, df], ignore_index=True)
        
        # Remove duplicatas e valores nulos
        df = df.drop_duplicates(subset=['title'])  # Remove duplicatas
        df = df.dropna(how='any')  # Remove valores nulos
        df["publication_date"] = pd.to_datetime(df["publication_date"], format='mixed', errors='coerce')
        
        
        # Salva no modo de adição (append), sem índice
        df.to_csv('../../data/notices.csv', index=False, encoding='utf-8')

    def process_item(self, item, spider):
        # Adiciona o item à lista
        self.items.append(dict(item))
        return item

    
class ScrapyG1Pipeline(object):
    def process_item(self, item, spider):
        
        if spider.name == 'g1':
            
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

class ScrapyCartacapitalPipeline(object):
    def process_item(self, item, spider):
        
        if spider.name == 'cartacapital':
      
            data = item['link'].split('/')
            item['category'] = data[3]
            item['source'] = "CartaCapital"
            
            match = re.search(r'(\d{2})\.(\d{2})\.(\d{4}) (\d{2})h(\d{2})', item['publication_date'])
            if match:
                day = int(match.group(1))
                month = int(match.group(2))
                year = int(match.group(3))
                hour = int(match.group(4))
                minute = int(match.group(5))

                dt_object = datetime(year, month, day, hour, minute)
                item['publication_date'] = dt_object.strftime('%Y-%m-%d %H:%M:%S')        
            
        return item

class ScrapyFolhaPipeline(object):
    def process_item(self, item, spider):
        
        if spider.name == 'folha':
        
            data = item['link'].split('/')
            item['category'] = data[3]
            item['source'] = "Folha"
            
            for field in ['title', 'text']:
                item[field] = item[field].replace('\t', ' ')
                item[field] = item[field].replace('\r', ' ')
                item[field] = item[field].replace('\n', ' ')
                item[field] = item[field].strip()
        
            months = {
                'jan': '01', 'fev': '02', 'mar': '03', 'abr': '04',
                'mai': '05', 'jun': '06', 'jul': '07', 'ago': '08',
                'set': '09', 'out': '10', 'nov': '11', 'dez': '12'
            }
            date_str = str(item['publication_date']).strip()
            date_str = re.sub(r'º', '', date_str) 
            date_str = re.sub(r'(\d+)°', r'\1', date_str)
            date_str = re.sub(r'(\d{4})', r'\1', date_str) 
            date_str = re.sub(r'(\d{2})([a-z]{3})(\d{4}).*(\d{2})(h\d{2})', r'\1-\2-\3 \4:\5:00', date_str)
            
            for month_name, month_num in months.items():
                date_str = date_str.replace(month_name, month_num)
            
            try:
                formatted_date = datetime.strptime(date_str, '%d.%m.%Y às %Hh%M')
            except:
                formatted_date = datetime.strptime(date_str, '%d.%m.%Y à %Hh%M')
            
            item['publication_date'] = formatted_date
        
        return item

