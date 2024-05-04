import os
import pandas as pd

from flask import Blueprint
from web_scrapping.src.scrapy_runner import ScrapyRunner
from recommendation.src.run_recomendation_system import RunRecomendationSystem
from recommendation.src.top_news_catcher import TopNewsCatcher

trigger = Blueprint('trigger', __name__, url_prefix='/trigger')

@trigger.route('/', methods=["POST"])
def triggerWebScrapping():
  ScrapyRunner.run()
  current_dir = os.getcwd()
  relative_path = os.path.join('web_scrapping', 'data', 'notices.csv')
  notices_path = os.path.join(current_dir, relative_path)
  print(f'>>>>>>> {notices_path}')
  dataset_top_news, df_to_recomendations = TopNewsCatcher().catch_top_news(path_to_csv=notices_path)

  # Retorna as x notícias principais e 3 notícias relacionadas a cada uma delas
  dataset = pd.read_csv(notices_path, low_memory=False, encoding="UTF-8")
  dataset_origin = dataset.iloc[:-1000]
  recommendation = RunRecomendationSystem(dataset=dataset_origin)
  dataset_topnews, dataset_recomendations = recommendation.run(dataset_top_news, df_to_recomendations)

  print(dataset_topnews.head())
  print(dataset_recomendations.head())
  return {}, 200