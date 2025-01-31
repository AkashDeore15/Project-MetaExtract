import nltk
from nltk.tokenize import word_tokenize, sent_tokenize

# Ensure the necessary NLTK resources are available
nltk.download('punkt', quiet=True)

def tokenize_words(cleaned_text):
    """Tokenize text into words."""
    try:
        return word_tokenize(cleaned_text)
    except Exception as e:
        print(f"Error in word tokenization: {e}")
        return []

def tokenize_sentences(cleaned_text):
    """Tokenize text into sentences."""
    try:
        return sent_tokenize(cleaned_text)
    except Exception as e:
        print(f"Error in sentence tokenization: {e}")
        return []
