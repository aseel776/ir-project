import math
from collections import defaultdict
from pandas import DataFrame
from utils.storing import store_dict, store_df

class Indexing():

    def __init__(self, corpus: list[dict]):
        self.corpus = corpus.copy()
    # ------------------------------------------------------
    def create_index(self):
        self.calc_all_tfs()

        inverted_index = self.create_inverted_index()
        idf = self.calc_idf(inverted_index)

        self.calc_all_tfidfs(idf)
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
        store_df(df, 'res/tf.csv')
    # ------------------------------------------------------ 
    def calc_tf(self, doc):
        tf = {}
        doc_terms = doc['text']

        for term in doc_terms:
            tf[term] = doc_terms.count(term) / len(doc_terms)

        return tf
    # ------------------------------------------------------
    def create_inverted_index(self):
        inverted_index = defaultdict(list)

        for doc in self.corpus:
            doc_terms = self.get_doc_terms(doc)
            for term in doc_terms:
                inverted_index[term].append(doc['id'])
    
        inverted_index = dict(inverted_index)
        store_dict(inverted_index, 'res/inverted_index.json')
        return inverted_index
    # ------------------------------------------------------
    def get_doc_terms(self, doc):
        doc_terms = set()
        doc_terms.update(doc['text'])
        return doc_terms
    # ------------------------------------------------------
    def calc_idf(self, inverted_index: dict):
        idf = {}
        docs_count = len(self.corpus)

        for term, doc_ids in inverted_index.items():
            idf[term] = math.log((docs_count / len(doc_ids)) + 1)

        df = DataFrame(idf, index=['idf'])
        store_df(df, 'res/idf.csv')
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
        store_df(df, 'res/tf_idf.csv')        
    # ------------------------------------------------------
    def calc_tfidf(self, idf, doc):
        tf_idf = {}
        doc_terms = doc['text']
        tf = self.calc_tf(doc)
        for term in doc_terms:
            tf_idf[term] = tf[term] * idf[term]
        return tf_idf
