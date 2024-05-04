import unittest
from datetime import datetime, timedelta
from scrapy_all.pipelines import ScrapyG1Pipeline

class ScrapyG1PipelineTests(unittest.TestCase):
    def setUp(self):
        self.pipeline = ScrapyG1Pipeline()

    def test_process_item_with_minutes(self):
        item = {
            'publication_date': 'minuto 10',
            # other item attributes
        }
        spider = type('Spider', (object,), {'name': 'g1'})
        current_time = datetime.now()
        expected_time = current_time - timedelta(minutes=10)

        processed_item = self.pipeline.process_item(item, spider)

        self.assertEqual(processed_item['publication_date'], expected_time)

    def test_process_item_with_hours(self):
        item = {
            'publication_date': 'hora 2',
            # other item attributes
        }
        spider = type('Spider', (object,), {'name': 'g1'})
        current_time = datetime.now()
        expected_time = current_time - timedelta(hours=2)

        processed_item = self.pipeline.process_item(item, spider)

        self.assertEqual(processed_item['publication_date'], expected_time)

    def test_process_item_with_yesterday(self):
        item = {
            'publication_date': 'ontem',
            # other item attributes
        }
        spider = type('Spider', (object,), {'name': 'g1'})
        current_time = datetime.now()
        expected_time = current_time - timedelta(days=1)

        processed_item = self.pipeline.process_item(item, spider)

        self.assertEqual(processed_item['publication_date'], expected_time)
        
    def test_process_item_with_days(self):
        item = {
            'publication_date': 'dia 2',
            # other item attributes
        }
        spider = type('Spider', (object,), {'name': 'g1'})
        current_time = datetime.now()
        expected_time = current_time - timedelta(days=2)

        processed_item = self.pipeline.process_item(item, spider)

        self.assertEqual(processed_item['publication_date'], expected_time) 
    
    def test_process_item_with_weeks(self):
        item = {
            'publication_date': 'semana 2',
            # other item attributes
        }
        spider = type('Spider', (object,), {'name': 'g1'})
        current_time = datetime.now()
        expected_time = current_time - timedelta(weeks=2)

        processed_item = self.pipeline.process_item(item, spider)

        self.assertEqual(processed_item['publication_date'], expected_time)
    
    def test_process_item_with_months(self):
        item = {
            'publication_date': 'mês 2',
            # other item attributes
        }
        spider = type('Spider', (object,), {'name': 'g1'})
        current_time = datetime.now()
        expected_time = current_time - timedelta(days=60)

        processed_item = self.pipeline.process_item(item, spider)

        self.assertEqual(processed_item['publication_date'], expected_time)
        
    def test_process_item_with_invalid_date(self):
        item = {
            'publication_date': 'invalid date',
            # other item attributes
        }
        spider = type('Spider', (object,), {'name': 'g1'})
        current_time = datetime.now()

        processed_item = self.pipeline.process_item(item, spider)

        self.assertEqual(processed_item['publication_date'], 'invalid date')
        
    def test_process_item_with_invalid_spider(self):
        item = {
            'publication_date': 'minuto 10',
            # other item attributes
        }
        spider = type('Spider', (object,), {'name': 'invalid_spider'})
        current_time = datetime.now()
        expected_time = current_time - timedelta(minutes=10)

        processed_item = self.pipeline.process_item(item, spider)

        self.assertEqual(processed_item['publication_date'], expected_time)
        
if __name__ == '__main__':
    unittest.main()