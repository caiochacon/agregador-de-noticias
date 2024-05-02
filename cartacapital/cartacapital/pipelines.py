# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import re
from datetime import datetime

class ParseCategory(object):
    def process_item(self, item, spider):
      
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


class CartacapitalPipeline:
    def process_item(self, item, spider):
        return item
