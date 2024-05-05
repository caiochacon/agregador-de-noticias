import sys
sys.path.append('..')
import pandas as pd
from importlib.machinery import SourceFileLoader
from agregador_de_noticias_recommendation_system.src.run_recomendation_system import RunRecomendationSystem
from agregador_de_noticias_recommendation_system.src.top_news_catcher import TopNewsCatcher

dataset = pd.read_csv("/home/vinicius_olzon/Documents/ENG_SOFTWARE/backend/flask_app/agregador_de_noticias_recommendation_system/dataset/noticiasGeradas.csv", low_memory=False, encoding="UTF-8")

dataset_origin = dataset.iloc[:-1000]
dataset_test = dataset.iloc[-1000:]

# Sistema de recomendação
recomendation_system = RunRecomendationSystem(dataset_origin)

catcher = TopNewsCatcher()
