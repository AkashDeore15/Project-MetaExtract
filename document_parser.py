import os
import logging
import json
from PyPDF2 import PdfReader
from docx import Document
from PIL import Image
import pytesseract
import fitz  # PyMuPDF
from pdf2image import convert_from_path

class DocumentParser:
    def __init__(self):
        self.text = ""

    def parse_pdf(self, file_path):
        """Extract text from a PDF file."""
        try:
            self.text = extract_text_from_pdf(file_path)
            return self.text
        except Exception as e:
            log_message(f"Error parsing PDF: {e}", level="error")
            return ""

    def parse_docx(self, file_path):
        """Extract text from a DOCX file."""
        try:
            self.text = extract_text_from_docx(file_path)
            return self.text
        except Exception as e:
            log_message(f"Error parsing DOCX: {e}", level="error")
            return ""

    def save_to_file(self, file_name):
        """Save extracted text to a plain text file."""
        try:
            save_text_to_file(self.text, file_name)
        except Exception as e:
            log_message(f"Error saving text to file: {e}", level="error")

    def save_to_json(self, file_name):
        """Save extracted text to a JSON file."""
        try:
            save_text_to_json({"text": self.text}, file_name)
        except Exception as e:
            log_message(f"Error saving text to JSON: {e}", level="error")

    def save_to_csv(self, data, file_name):
        """Save data to a CSV file."""
        try:
            save_text_to_csv(data, file_name)
        except Exception as e:
            
            log_message(f"Error saving data to CSV: {e}", level="error")
# Utility functions

def extract_text_from_pdf(file_path):
    """Extract text from a PDF file using PyPDF2 and PyMuPDF as fallback."""
    try:
        reader = PdfReader(file_path)
        text = "".join(page.extract_text() for page in reader.pages)
        return text
    except Exception as e:
        log_message(f"PyPDF2 failed: {e}", level="error")
        # Fallback to PyMuPDF
        try:
            with fitz.open(file_path) as pdf:
                text = "".join(page.get_text() for page in pdf)
                return text
        except Exception as fallback_error:
            log_message(f"PyMuPDF failed: {fallback_error}", level="error")
            return ""

def extract_text_from_docx(file_path):
    """Extract text from a DOCX file."""
    try:
        doc = Document(file_path)
        return "\n".join(paragraph.text for paragraph in doc.paragraphs)
    except Exception as e:
        log_message(f"Error reading DOCX: {e}", level="error")
        return ""

def extract_text_with_ocr(pdf_path):
    """Extract text from image-based PDFs using OCR."""
    try:
        pages = convert_from_path(pdf_path)
        text = "".join(pytesseract.image_to_string(page) for page in pages)
        return text
    except Exception as e:
        log_message(f"OCR failed: {e}", level="error")
        return ""

def save_text_to_file(text, file_name):
    """Save text content to a plain text file."""
    with open(file_name, "w") as file:
        file.write(text)

def save_text_to_json(data, file_name):
    """Save data to a JSON file."""
    with open(file_name, "w") as file:
        json.dump(data, file, indent=4)
def save_text_to_csv(data, file_name):
    """Save data to a CSV file."""
    with open(file_name, mode='w', newline='', encoding='utf-8') as f:
        #writer = csv.writer(f)
        writer.writerow(data.keys())  # Write header
        writer.writerow(data.values())  # Write values

def log_message(message, level="info"):
    """Log messages to a file and optionally print to console."""
    levels = {"info": logging.info, "error": logging.error}
    levels.get(level, logging.info)(message)
    print(message)

# Logging configuration
logging.basicConfig(
    filename="document_parser.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

if __name__ == "__main__":
    parser = DocumentParser()
'''
    # Paths to sample files
    #pdf_file_path = "./sample_invoice.pdf"
    #docx_file_path = "./sample_purchase_order.docx"

    # PDF parsing
    pdf_text = parser.parse_pdf(pdf_file_path)
    if not pdf_text:
        log_message("Attempting OCR extraction.", level="info")
        pdf_text = extract_text_with_ocr(pdf_file_path)

    # DOCX parsing
    docx_text = parser.parse_docx(docx_file_path)

    # Save outputs
    parser.save_to_file("output_text.txt")
    parser.save_to_json("output.json")
    parser.save_to_csv({"pdf_text": pdf_text, "docx_text": docx_text}, "output.csv")

    # Log extracted content
    log_message(f"Extracted PDF Text: {pdf_text[:100]}...")
    log_message(f"Extracted DOCX Text: {docx_text[:100]}...")
'''