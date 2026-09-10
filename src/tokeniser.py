import string
import nltk
from nltk.corpus import stopwords
nltk.downoad('stopwords')

def tokenise(text:str):
    """
    Convert raw text into a list of normalized tokens.

    Steps:
    1. Convert text to lowercase.
    2. Extract words.
    3. Remove stopwords.
    """
    text = text.lower()
    punctToRemove = "!#$%&()*+,./:;<=>?@[\\]^_`{|}~"
    translator = str.maketrans("", "", punctToRemove)
    cleanText = text.translate(translator)
    words = cleanText.split()
    stopwords = set(stopwords.words('english'))
    filtered = [word for word in words if word not in stopwords]
    return filtered



