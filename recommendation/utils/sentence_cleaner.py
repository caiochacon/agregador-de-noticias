import spacy
import string
import re


class SentenceCleaner:
   
   
    def __init__(self):     

        self.nlp = spacy.load('pt_core_news_lg')
        stop_words = list(spacy.lang.pt.stop_words.STOP_WORDS)
        punct = list(string.punctuation)

        self.remove_chars =  stop_words + punct + ["Mundo Folha", "Opinião Folha", "Folha" , "Opinião", '-', "Painel"]

    def clear_sentence(self, sentence):

        doc = self.nlp.tokenizer(str(sentence))
        tokens_list = [s.text for s in doc if s.text not in self.remove_chars]
        preprocessed_sentence = ' '.join(tokens_list)
        preprocessed_sentence = self.__remove_dates(preprocessed_sentence)
        preprocessed_sentence = self.__remove_numbers(preprocessed_sentence)

        return preprocessed_sentence.strip()

    def __remove_dates(self, text):
        pattern = r'\d{1,2}[\/\.-]\d{1,2}[\/\.-]\d{2,4}|\d{1,2}\s(?:de\s)?(?:janeiro|fevereiro|março|abril|maio|junho|julho|agosto|setembro|outubro|novembro|dezembro)\s\d{2,4}'
        return re.sub(pattern, '', text)

    def __remove_numbers(self, text):
        sentence_without_numbers = re.sub(r'\d+', '', text)
        return sentence_without_numbers