from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
import string


def tokenize_remove_stopwords(sentence):
    stop_words = set(stopwords.words('english'))
    word_tokens = word_tokenize(sentence)
    filtered_sentence_tokens = [w for w in word_tokens if not w in stop_words]
    no_punctuation_tokens = list(filter(lambda token: token not in string.punctuation, filtered_sentence_tokens))
    return no_punctuation_tokens


