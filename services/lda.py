#import libraries
import os
import re
import json
import gensim
from gensim.corpora import Dictionary
from gensim.models import LdaModel
from contants.stopwords import all_stopwords
import services.data_cleaner as data_cleaner

class TopicExtractor:
    corpus = None
    dictionary = None
    lda_model = None

    def clean_content(self, content):
        """
        Function to clean unecessary data and stopwords, punctuations from the content

        Parameters:
            content (str): Text content to be cleaned

        Returns:
            stemmed_tokens (list): List of tokens after cleaning, lemmatization and stemming
        """
        text_tf = data_cleaner.DataCleaner()
        stemmed_tokens = text_tf.parse_method(content.lower())
        return stemmed_tokens
    
    def make_bigrams(self, stemmed_tokens):
        """
        Function to prepare bigrames from the token list

        Parameters:
            stemmed_tokens (str): Tokens for bigram preparation

        Returns:
            List (list): List of bigrames prepared
        """

        bigram = gensim.models.Phrases([stemmed_tokens], min_count=5, threshold=100)
        bigram_mod = gensim.models.phrases.Phraser(bigram)
        return [bigram_mod[doc] for doc in [stemmed_tokens]]

    def build_corpus(self, data_words_bigrams):
        """
        Function for finding topics from given content

        Parameters:
            data_words_bigrams (object list): Build content corpus from the token bigrams

        """

        self.dictionary = Dictionary(data_words_bigrams)
        self.corpus = [self.dictionary.doc2bow(doc) for doc in data_words_bigrams]

    def get_document_topic_table(self):
        """
        Function to get the topics from the LDA model

        Returns:
            key_words (list): Extracted keywords from LDA model

        """

        # Init output
        # Get main topics in document
        key_words = []
        for i, row_list in enumerate(self.lda_model[self.corpus]):
            row = sorted(row_list, key=lambda x: (x[1]), reverse=True)
            topic_num=row[0][0]
            wp = self.lda_model.show_topic(topic_num)
            key_words = [word for word, prop in wp]
        
        return key_words
    
    def build_lda_model(self):
        # build LDA from corpus
        self.lda_model = LdaModel(corpus=self.corpus, id2word=self.dictionary, num_topics=10, random_state=50, chunksize=100, passes=50)

    def get_topics(self, content):
        """
        Function for finding topics from given content

        Parameters:
            content (str): Text content from which topics will be extracted

        Returns:
            topic_list (list): List of topics extracted using LDA algorithm

        """

        stemmed_tokens = self.clean_content(content)
        data_words_bigrams = self.make_bigrams(stemmed_tokens)
        self.build_corpus(data_words_bigrams)
        self.build_lda_model()
        topic_list = self.get_document_topic_table()
        return topic_list