import sys
sys.path.append('..')

import pytest
from utils.sentence_cleaner import SentenceCleaner

@pytest.fixture
def cleaner():
    return SentenceCleaner()

def test_clear_sentence(cleaner):
    # Test with a sentence containing stopwords, punctuation, and custom remove_chars
    sentence = "O mundo está cheio de opiniões, e a Folha de São Paulo tem muitas delas. - Opinião Folha"
    expected_result = "O mundo cheio opiniões São Paulo muitas delas"
    assert cleaner.clear_sentence(sentence) == expected_result

    # Test with a sentence containing dates
    sentence_with_dates = "A reunião está marcada para 25/05/2023 às 14:30."
    expected_result_without_dates = "A reunião marcada"
    assert cleaner.clear_sentence(sentence_with_dates) == expected_result_without_dates

    # Test with a sentence containing numbers
    sentence_with_numbers = "Hoje é o dia 31 de dezembro de 2022 e está fazendo 20 graus."
    expected_result_without_numbers = "Hoje dia dezembro fazendo graus"

    assert cleaner.clear_sentence(sentence_with_numbers) == expected_result_without_numbers

    # Test with an empty sentence
    empty_sentence = ""
    assert cleaner.clear_sentence(empty_sentence) == ""

    # Test with a sentence containing only punctuation
    punctuation_only = "?!.,;:"
    assert cleaner.clear_sentence(punctuation_only) == ""

    # Test with a sentence containing additional words
    ignore_words_with_additional = "Folha, Opinião, Opinião Folha, not_to_ignore"
    assert cleaner.clear_sentence(ignore_words_with_additional) == "not_to_ignore"