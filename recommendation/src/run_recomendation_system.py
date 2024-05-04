import sys
import os
import pickle

sys.path.append('..')

import pandas as pd

from sklearn.feature_extraction.text import TfidfVectorizer

from utils.sentence_cleaner import SentenceCleaner
from utils.data_scorer_calculator import DataScorerCalculator
from utils.sentences_similarity_calculator import SentenceSimilarityCalculator

COEF_WHEIGHT_DATE = 20

class RunRecomendationSystem:

    def __init__(self, path_to_vectorizer = "../models/tfidf_vectorizer.pkl"):

        self.path_to_vectorizer = path_to_vectorizer

        self.data_scorer_calculator = DataScorerCalculator()
        self.sentece_cleaner = SentenceCleaner()
        self.sentences_sym_calculator = SentenceSimilarityCalculator()

        if os.path.exists(self.path_to_vectorizer):

            with open(self.path_to_vectorizer, 'rb') as file:
                self.tfidf_vectorizer = pickle.load(file)

        else:
           self.tfidf_vectorizer =  self.train()

    # Docs são um dataframe [title, publication_date]

    def run(self, dataset_sentences, new_docs):
        
        self.dataset_sentences = dataset_sentences.copy()

        self.new_doc = new_docs.copy()
        

        self.new_doc['publication_date'] = pd.to_datetime(self.new_doc['publication_date'], format='mixed', errors='coerce')

        self.new_doc['normalized_data_scores'] = self.data_scorer_calculator.calculate_data_score(self.new_doc['publication_date'])
        self.new_doc.loc[:, 'sentences'] = self.new_doc.loc[:, 'title'].apply(self.sentece_cleaner.clear_sentence)

        self.dataset_sentences.loc[:, 'sentences'] = dataset_sentences.loc[:, 'title'].apply(self.sentece_cleaner.clear_sentence)
        #new_sent = self.sentece_cleaner.clear_sentence(raw_sentence)
        #new_sent = self.tfidf_vectorizer.transform([new_sent])

        new_docs_tfidf_matrix = self.tfidf_vectorizer.transform(self.new_doc['sentences'].values)
        self.idx_recomendations = []

        for new_sentence in self.dataset_sentences['sentences'].values:
            new_sent = self.sentece_cleaner.clear_sentence(new_sentence)
            new_sent = self.tfidf_vectorizer.transform([new_sent])
            self.idx_recomendations.extend(self.sentences_sym_calculator.sym_by_date(new_sent, new_docs_tfidf_matrix, self.new_doc['normalized_data_scores'].values, 20, 3))

        dataset_recomendations = pd.DataFrame(self.new_doc.iloc[self.idx_recomendations])

        return self.dataset_sentences, dataset_recomendations
    
    def show_recomendations(self):

        print(f'Alvo -> {self.raw_sentence}')
        print('\nTop-5 similarity rate:\n')

        for idx in self.idx_recomendations:
            print(self.new_doc["title"].values[idx])

    def train(self, path_to_csv = "../../dataset/notices.csv"):

        self.dataset = pd.read_csv(path_to_csv, low_memory=False, encoding="UTF-8")

        self.dataset['publication_date'] = pd.to_datetime(self.dataset['publication_date'], format='mixed', errors='coerce')
        self.tfidf_vectorizer = TfidfVectorizer()


        self.dataset['normalized_data_scores'] = self.data_scorer_calculator.calculate_data_score(self.dataset['publication_date'])
        self.dataset.loc[:, 'sentences'] = self.dataset.loc[:, 'title'].apply(self.sentece_cleaner.clear_sentence)

        self.tfidf_matrix = self.tfidf_vectorizer.fit_transform(self.dataset['sentences'].values)

        with open(self.path_to_vectorizer, 'wb') as file:
            pickle.dump(self.tfidf_vectorizer, file)

        print(f"...Model Vectorize Saved in: {self.path_to_vectorizer} ...")

        return self.tfidf_vectorizer

