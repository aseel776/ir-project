import math
import os
from collections import defaultdict
from pandas import DataFrame
from nltk.tokenize import word_tokenize
from utils.storing import store_dict, store_df, store_matrix
from sklearn.feature_extraction.text import TfidfVectorizer

class Indexing():

    def __init__(self, corpus: list[dict], directory: str):
        self.corpus = corpus.copy()
        self.directory = directory
        if not os.path.exists(directory):
            os.makedirs(directory)
    # ------------------------------------------------------
    def create_index(self):
        self.calc_all_tfs()

        inverted_index = self.create_inverted_index()
        idf = self.calc_idf(inverted_index)

        self.calc_all_tfidfs(idf)
        self.calc_scikit_tfidfs()
    # ------------------------------------------------------
    def calc_all_tfs(self):    
        tf_list = []
        keys = []

        for doc in self.corpus:
            tf = self.calc_tf(doc)
            tf_list.append(tf)
            keys.append(doc['id'])
            
        df = DataFrame(tf_list, index=keys)
        df = df.fillna(0)        
        store_df(df, f'{self.directory}/tf.csv')
    # ------------------------------------------------------ 
    def calc_tf(self, doc):
        tf = {}
        text = word_tokenize(doc['text'])

        for word in text:
            tf[word] = text.count(word) / len(text)

        return tf
    # ------------------------------------------------------
    def create_inverted_index(self):
        inverted_index = defaultdict(list)

        for doc in self.corpus:
            doc_terms = self.get_doc_terms(doc)
            for term in doc_terms:
                inverted_index[term].append(doc['id'])
    
        inverted_index = dict(inverted_index)
        store_dict(inverted_index, f'{self.directory}/inverted_index.json')
        return inverted_index
    # ------------------------------------------------------
    def get_doc_terms(self, doc):
        text = word_tokenize(doc['text'])
        doc_terms = set()
        doc_terms.update(text)
        return doc_terms
    # ------------------------------------------------------
    def calc_idf(self, inverted_index: dict):
        idf = {}
        docs_count = len(self.corpus)

        for term, doc_ids in inverted_index.items():
            idf[term] = math.log((docs_count / len(doc_ids)) + 1)

        df = DataFrame(idf, index=['idf'])
        store_df(df, f'{self.directory}/idf.csv')
        return idf
    # ------------------------------------------------------
    def calc_all_tfidfs(self, idf):
        tf_idf_list = []
        keys = []
        for doc in self.corpus:
            tf_idf = self.calc_tfidf(idf, doc)
            tf_idf_list.append(tf_idf)
            keys.append(doc['id'])
        df = DataFrame(tf_idf_list, index=keys)
        df = df.fillna(0)
        store_df(df, f'{self.directory}/tf_idf.csv')        
    # ------------------------------------------------------
    def calc_tfidf(self, idf, doc):
        tf_idf = {}
        doc_terms = self.get_doc_terms(doc)
        tf = self.calc_tf(doc)
        for term in doc_terms:
            tf_idf[term] = tf[term] * idf[term]
        return tf_idf
    # ------------------------------------------------------
    def calc_scikit_tfidfs(self):
        ids = [item['id'] for item in self.corpus]
        docs = [item['text'] for item in self.corpus]

        vectorizer = TfidfVectorizer()
        tfidf_matrix = vectorizer.fit_transform(docs)

        df = DataFrame(
            tfidf_matrix.toarray(), 
            index = ids,
            columns = vectorizer.get_feature_names_out()
            )
        store_df(df, f'{self.directory}/tf_idf-scikit.csv')
        store_matrix(tfidf_matrix, f'{self.directory}/tf_idf-scikit.pkl')
    # ------------------------------------------------------
