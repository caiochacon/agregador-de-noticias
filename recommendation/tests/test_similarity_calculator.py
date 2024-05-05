import sys
sys.path.append('..')

import numpy as np
import pytest
from utils.sentences_similarity_calculator import SentenceSimilarityCalculator

def test_sym_by_date():
    # Create an instance of SentenceSimilarityCalculator
    similarity_calculator = SentenceSimilarityCalculator()

    # Example data
    sentence = np.array([[1, 0, 0]])
    doc = np.array([[1, 1, 0], [0, 1, 1], [1, 0, 1], [0, 1, 0], [0, 0, 1]])
    date_scores = np.array([0.2, 0.3, 0.1, 0.4, 0.5])
    coef_date = 10
    len_return_list = 5
    
    # Verify if the indices of most similar sentences by date are correct
    expected_result = np.array([2, 0, 1, 3, 4])
    assert np.array_equal(similarity_calculator.sym_by_date(sentence, doc, date_scores, coef_date, len_return_list), expected_result)
