import re
import pandas as pd
import os,sys
import string 
import gensim.corpora as corpora
from gensim.corpora import Dictionary
from contants.stopwords import all_stopwords
reg_dot = re.compile(r"(.*)¨(.)(.*)")

class DataCleaner:
    """ 
    DataCleaner class for is for text cleaning, stopword removal and tokenozation.
    Attributes: 
        string_input (str): Extracted text data
    """
    
    def parse_method(self, string_input):
        """
        Function to Tokenize. The Function calls _sent_tokenize to for replacing punctuations,_word_tokenize for lemmatization, 
        _preprocess_string for stopwords removal, _const_count for valid tokens based on size.

        Paramters:
            string_input (str): Extracted articles

        Returns:
            valid_tokens (list): List of valid tokens

        """
        word_tokens = [token for sentence in self.__sent_tokenize(string_input) for token in self.__word_tokenize(self.__preprocess_string(sentence)) if (token not in all_stopwords)]
        valid_tokens, _ = self.__const_count(word_tokens, 3)
        return valid_tokens


    def __preprocess_string(self, sentence):
        """
        Function for text cleaning by removing stopwords, numerical character sets, http links

        Parameters:
            sentence (str): Sentence for the text after sentence tokenization.

        Returns:
            sentence (str): Senetence post cleaning.

        """
        if sentence == '':
            return ''
        sentence = re.sub(r'https?:\/\/.*', 'LINK', sentence)  # Remove hyperlinks
        sentence = re.sub(r'[0-9]+', '', sentence) # replace numbers with NUM
        return sentence

    def __sent_tokenize(self, doc):
        """
        Function for replacing English punctuation(if present)

        Parameters:
            doc (str): content

        Returns:
            sent (str): Sentences

        """
        for sent in doc.replace("?", "।").replace("！", "।").replace("!", "।").split("।"):
            yield sent.strip()


    def __word_tokenize(self, sent):
        """
        Function for lemmatisation

        Parameters:
            sent (str): Tokenized words

        Returns:
            token (str): Lemmatized Tokens

        """

        for token in sent.split(" "):
            # w = Word(token)
            # yield w.lemmatize()
            # yield lemmatize(token)
            # yield lemmatizer.lemmatize(token)
            token = re.sub(f"[{re.escape(string.punctuation)}]", "", token)
            token = re.sub(r'\[.*?\]', '', token)
            token = re.sub(r'\(.*?\)', '', token)
            token = re.sub(r"\s+", " ", token)
            token = re.sub(r'\w*\d\w*', '', token)
            token = re.sub(r"\w+…|…", "", token)  # Remove ellipsis (and last word)
            yield reg_dot.sub(r'\1\2\3', token)


    def __const_count(self, tokens, min_num):
        """
        Function for extracting valid tokens

        Parameters:
            tokens (str): String tokens
            min_num (int): Size to consider for valid token size

        Returns:
            token (str): Valid Tokens

        """
        valid_tokens = []
        invalid_tokens = []
        for token in tokens:
            if (len(token) >= min_num):
                valid_tokens.append(token)
            else:
                invalid_tokens.append(token)
        return valid_tokens, invalid_tokens