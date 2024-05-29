from nltk.corpus import stopwords, wordnet
from nltk.tokenize import word_tokenize
from nltk.stem import LancasterStemmer, WordNetLemmatizer
from nltk import pos_tag
from string import punctuation
from utils.converting import convert_to_str

class TextProcessor:

    def process(self, text: str):
        # first tolower
        text = text.lower()
        # then remove punctuations & numbers
        text = self.remove_punctuation(text)
        text = self.remove_numbers(text)
        # tokenize
        tokens = self.tokenize(text)
        # remove stop words from tokens
        filtered_tokens = self.remove_stopwords(tokens)
        # stemming
        # stemmed_tokens = self.stem(filtered_tokens)
        # NOTE!!! when uncommenting stemming remember to comment lemmatizing and vice versa
        # lemmatizing
        lemmatized_tokens = self.lemmatize(filtered_tokens)
        # get them back into one string
        return convert_to_str(lemmatized_tokens)
    
    def remove_punctuation(self, text: str):
        table = str.maketrans('', '', punctuation)
        filtered_text = text.translate(table)
        return filtered_text
    
    def remove_numbers(self, text: str):
      import re
      return re.sub(r"\d+", "", text)
    
    def tokenize(self, text: str):
        return word_tokenize(text)
    
    def remove_stopwords(self, words: list[str]):
        stop_words = stopwords.words('english')
        filtered_text = [word for word in words if word not in stop_words]
        return filtered_text

    def stem(self, tokens: list[str]):
        # NOTE!!! import it from nltk.stem
        # stemmer = PorterStemmer()
        stemmer = LancasterStemmer()
        stemmed_words = [stemmer.stem(token) for token in tokens]
        return stemmed_words
    
    def lemmatize(self, tokens: list[str]):
        # get part-of-speech tags first
        pos_tags = pos_tag(tokens)
        lemmatizer = WordNetLemmatizer()
        lemmatized_words = []
        for word, tag in pos_tags:
            # transform into wordnet pos form
            wn_pos = self.get_wordnet_pos(tag)
            lemma = lemmatizer.lemmatize(word, wn_pos)
            lemmatized_words.append(lemma)
        return lemmatized_words
    
    def get_wordnet_pos(self, tag_parameter):
        tag = tag_parameter[0].upper()
        tag_dict = {
            "J": wordnet.ADJ,
            "N": wordnet.NOUN,
            "V": wordnet.VERB,
            "R": wordnet.ADV
            }
        return tag_dict.get(tag, wordnet.NOUN)
