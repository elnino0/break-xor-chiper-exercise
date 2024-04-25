import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import words

nltk.download('punkt')
nltk.download('words')

set_of_words = set(words.words())


def is_text(text):
    tokens = word_tokenize(text)
    # Filter out non-word tokens
    filter_tokens = [token for token in tokens if token.isalpha()]
    filter_tokens = [token for token in filter_tokens if token in set_of_words]

    if float(len(filter_tokens)) / float(len(tokens)) > 0.5:
        return True

    return False
