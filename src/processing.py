from nltk import *
from nltk.corpus import stopwords
from nltk.tokenize import sent_tokenize, word_tokenize, TreebankWordTokenizer, WordPunctTokenizer
from nltk.stem.porter import *

def remove_stopwords(words):
    english_sw = stopwords.words('english')
    return [word for word in words if word not in english_sw]

def string_tokenize(string):
    tokenizer=TreebankWordTokenizer()
    tokens = tokenizer.tokenize(string.lower())
    return [token for token in tokens if token.isalpha()]
    
def stemming(words):
	lis = []
	stemmer = PorterStemmer()
	for i in range(len(words)):
		lis.append(stemmer.stem(words[i]))
	return lis

def process_0(sentence):
	return string_tokenize(sentence)

def process_1(sentence):
	return remove_stopwords(string_tokenize(sentence))

def process_2(sentence):
	return stemming(string_tokenize(sentence))

def process_3(sentence):
	return stemming(remove_stopwords(string_tokenize(sentence)))
