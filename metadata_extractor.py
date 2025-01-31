import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.probability import FreqDist

nltk.download('punkt', quiet=True)
nltk.download('stopwords', quiet=True)

class MetadataExtractor:
    def __init__(self, text):
        self.text = text
        self.tokens = []
        self.filtered_tokens = []
        self.frequent_words = []

    def tokenize_text(self):
        self.tokens = word_tokenize(self.text)

    def remove_stopwords(self):
        stop_words = set(stopwords.words('english'))
        self.filtered_tokens = [word for word in self.tokens if word.lower() not in stop_words]

    def extract_frequent_words(self, top_n=10):
        fdist = FreqDist(self.filtered_tokens)
        self.frequent_words = fdist.most_common(top_n)
