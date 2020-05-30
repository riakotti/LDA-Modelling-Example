# most of code from https://github.com/priya-dwivedi/Deep-Learning

import gensim
from gensim.utils import simple_preprocess
from gensim.parsing.preprocessing import STOPWORDS
from nltk.stem import WordNetLemmatizer, SnowballStemmer
from nltk.stem.porter import *
import pandas as pd

import numpy as np
import nltk
nltk.download('wordnet')


class LDAtext:
    def __init__(self):
        self.stemmer = SnowballStemmer("english")

    def text_preprocess_(self, documents):

        processed_docs = []
        # newsgroups_train.data
        for doc in documents:
            processed_docs.append(preprocess(doc))
        return processed_docs


    def lemmatize_stemming(self, text):
        return self.stemmer.stem(WordNetLemmatizer().lemmatize(text, pos='v'))

    # Tokenize and lemmatize
    def preprocess(self, text):
        result = []
        for token in gensim.utils.simple_preprocess(text):
            if token not in gensim.parsing.preprocessing.STOPWORDS and len(
                    token) > 3:
                result.append(lemmatize_stemming(token))

        return result

    def train(self,
              documents,
              number_of_topics=8,
              number_of_passes=10,
              number_of_workers=2):
        processed_docs = self.text_preprocess_(documents)

        self.dictionary = gensim.corpora.Dictionary(processed_docs)

        bow_corpus = [dictionary.doc2bow(doc) for doc in processed_docs]

        self.lda_model = gensim.models.LdaMulticore(
            bow_corpus,
            num_topics=number_of_topics,
            id2word=dictionary,
            passes=number_of_passes,
            workers=number_of_workers)

    def predict(self, unseen_doc):

        # Data preprocessing step for the unseen document
        bow_vector = self.dictionary.doc2bow(self.preprocess(unseen_doc))
        return self.lda_model[bow_vector]

    def topics(self):
        '''
        For each topic, we will explore the words occuring in that topic and its relative weight
        '''
        for idx, topic in self.lda_model.print_topics(-1):
            print("Topic: {} \nWords: {}".format(idx, topic))
            print("\n")
