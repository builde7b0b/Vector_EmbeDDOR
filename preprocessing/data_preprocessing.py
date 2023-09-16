import pandas as pd 
import nltk 
from nltk.corpus import stopwords 
from nltk.tokenize import word_tokenize 
from nltk.stem import PorterStemmer 

nltk.download('punkt')
nltk.download('stopwords')

# Load the data 
data = pd.read_csv('product_descriptions.csv')

# Tokenization and preprocessing 
stop_words = set(stopwords.words('english'))
stemmer = PorterStemmer()

def preprocess_text(text):
    tokens = word_tokenize(text)
    tokens = [stemmer.stem(word.lower()) for word in tokens if word.isalpha() and word.lower() not in stop_words]
    return ' '.join(tokens)

data['processed_description'] = data['description'].apply(preprocess_text)
