from nltk.stem import WordNetLemmatizer
import nltk

# Ensure necessary resources are available
nltk.download('wordnet', quiet=True)
nltk.download('omw-1.4', quiet=True)

def lemmatize_text(cleaned_text):
    """Lemmatize text for consistent representation."""
    lemmatizer = WordNetLemmatizer()
    lemmatized_words = []

    try:
        for word in cleaned_text.split():
            lemmatized_word = lemmatizer.lemmatize(word) 
            lemmatized_words.append(lemmatized_word)
        return " ".join(lemmatized_words)
    except Exception as e:
        print(f"Error in lemmatization: {e}")
        return cleaned_text
