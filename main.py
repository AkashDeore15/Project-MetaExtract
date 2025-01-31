import os
from document_parser import DocumentParser
from text_cleaner import clean_text
from tokenizer import tokenize_words, tokenize_sentences
from lemmatizer import lemmatize_text
from metadata_extractor import MetadataExtractor
import argparse
import tkinter as tk
from tkinter import filedialog

def process_document(file_path):
    file_type = os.path.splitext(file_path)[1].lower()  # Extract file extension

    parser = DocumentParser()

    # Step 1: Extract Text
    if file_type == ".pdf":
        raw_text = parser.parse_pdf(file_path)
    elif file_type == ".docx":
        raw_text = parser.parse_docx(file_path)
    else:
        print("Unsupported file type.")
        return None
    
    # Step 2: Clean Text
    cleaned_text = clean_text(raw_text)

    # Step 3: Tokenize
    word_tokens = tokenize_words(cleaned_text)
    sentence_tokens = tokenize_sentences(cleaned_text)

    # Step 4: Lemmatize
    lemmatized_words = lemmatize_text(word_tokens)

    # Step 5: Save Results
    parser.text = " ".join(lemmatized_words)  # Update parser text for saving
    #parser.save_to_file("processed_output.txt")
    #parser.save_to_json("processed_output.json")
    
    extractor = MetadataExtractor(parser.text)
    extractor.tokenize_text()
    extractor.remove_stopwords()
    extractor.extract_frequent_words()

    # Output results
    print(f"Lemmatized Text: {' '.join(lemmatized_words)[:100]}...")
    print(f"Tokenized Sentences: {sentence_tokens[:2]}...")  # First two sentences
    print("Frequent Words:", extractor.frequent_words)
    
    # Collecting results
    results = {
        "cleaned_text": cleaned_text,
        "tokenized_sentences": sentence_tokens,
        "lemmatized_tokens": lemmatized_words,
        "frequent_words": extractor.frequent_words,
    }

    
   # Step 7: Output Formatting
    output_file = "output_data.json"
    parser.save_as_json(results, output_file)

    output_file = "output_data.csv"
    parser.save_as_csv(results, output_file)

    return " ".join(lemmatized_words)

def browse_file():
    """Opens a file dialog for the user to select a file."""

    file_path = filedialog.askopenfilename(
        filetypes=[("Document Files", "*.pdf *.docx")]
    )
    if file_path:
        process_document(file_path)

if __name__ == "__main__":
    '''
    # Provide file path and type
    file_path = "./sample_invoice.pdf"  # Replace with actual file path
    file_type = "pdf"
    output_format = "json"  # Change to "csv" for CSV output
    output_file = "output_data.json" if output_format == "json" else "output_data.csv"
    text = process_document(file_path, file_type, output_format, output_file)
    '''
    # Argument parsing
    root = tk.Tk()
    root.withdraw()  # Hide the main window

    browse_button = tk.Button(text="Select File", command=browse_file)
    browse_button.pack()

    root.mainloop()
 