from nltk.corpus import stopwords, wordnet
from nltk.tokenize import word_tokenize
from nltk.stem import LancasterStemmer, WordNetLemmatizer
from nltk import pos_tag
from string import punctuation

class TextProcessor:

    def __init__(self):
        print('init')

    def start_processing(self, text: str):
        print('start')
        # first tolower
        text = text.lower()
        print(text)
        # then remove punctuations
        text = self.remove_punctuation(text)
        print(text)
        # tokenize
        tokens = self.tokenize(text)
        print(tokens)
        # remove stop words from tokens
        filtered_tokens = self.remove_stopwords(tokens)
        print(filtered_tokens)
        # stemming
        stemmed_tokens = self.stem(filtered_tokens)
        print(stemmed_tokens)
        # lemmatizing
        lemmatized_tokens = self.lemmatize(filtered_tokens)
        print(lemmatized_tokens)
    
    def remove_punctuation(self, text: str):
        print('remove punctuation')
        table = str.maketrans('', '', punctuation)
        filtered_text = text.translate(table)
        return filtered_text
    
    def tokenize(self, text: str):
        print('tokenize')
        return word_tokenize(text)
    
    def remove_stopwords(self, words: list[str]):
        print('remove stopwords')
        stop_words = stopwords.words('english')
        filtered_text = [word for word in words if word not in stop_words]
        return filtered_text

    def stem(self, tokens: list[str]):
        print('stemming')
        # import it from nltk.stem
        # stemmer = PorterStemmer()
        stemmer = LancasterStemmer()
        stemmed_words = [stemmer.stem(token) for token in tokens]
        return stemmed_words
    
    def lemmatize(self, tokens: list[str]):
        print('lemmatizing')
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
