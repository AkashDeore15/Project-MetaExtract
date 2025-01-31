import re

def clean_text(raw_text):
    """Remove unnecessary characters and normalize text."""
    try:
        # Remove special characters, multiple spaces, and extra whitespace
        cleaned_text = re.sub(r"[^a-zA-Z0-9\s]", "", raw_text)  # Keep only alphanumerics
        cleaned_text = re.sub(r"\s+", " ", cleaned_text)  # Collapse multiple spaces
        return cleaned_text.strip()
    except Exception as e:
        print(f"Error in cleaning text: {e}")
        return raw_text
