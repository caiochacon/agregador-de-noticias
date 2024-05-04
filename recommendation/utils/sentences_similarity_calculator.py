import numpy as np
from sklearn.metrics.pairwise import cosine_similarity


class SentenceSimilarityCalculator:

    def sym_M(self, sentence, doc):
        return  np.argsort(cosine_similarity(sentence, doc), kind='quicksort')[0][-5:][::-1]

    def sym_by_date(self, sentence, doc, date_scores, coef_date, len_return_list):

        similarities = cosine_similarity(sentence, doc)[0]
        weighted_similarities = similarities - (date_scores * coef_date)
        sorted_indices = np.argsort(weighted_similarities, kind='quicksort')[::-1]
        
        return  sorted_indices[:len_return_list]