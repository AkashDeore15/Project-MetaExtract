# Project-MetaExtract

An automation platform designed to extract metadata from documents by leveraging Natural Language Processing (NLP) and Machine Learning (ML) capabilities, tailored for the Wholesale Payments business.

## Overview

Project-MetaExtract aims to streamline the extraction of pertinent metadata from various document types, enhancing data processing efficiency in financial operations. By utilizing advanced NLP and ML techniques, the platform automates the identification and retrieval of key information from documents such as invoices and purchase orders.

## Features

- **Document Parsing**: Processes and converts documents into machine-readable text.
- **Text Cleaning**: Removes irrelevant data and normalizes text for analysis.
- **Tokenization and Lemmatization**: Breaks down text into tokens and reduces them to their base forms.
- **Metadata Extraction**: Identifies and extracts essential metadata from processed text.
- **Output Formatting**: Structures the extracted metadata into a standardized format for downstream applications.

## Getting Started

### Prerequisites

- **Python 3.x**: Ensure Python is installed on your system. Download it from the [official Python website](https://www.python.org/downloads/).
- **Required Libraries**: Install the necessary Python libraries using the provided `requirements.txt` file.

### Installation

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/AkashDeore15/Project-MetaExtract.git
   cd Project-MetaExtract
   ```

2. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

### Usage

1. **Prepare Your Documents**: Place the documents you wish to process in the designated input directory.

2. **Run the Main Script**:
   ```bash
   python main.py
   ```

3. **View Results**: The extracted metadata will be available in the output files generated by the platform.

## File Structure

- `main.py`: Orchestrates the workflow of the platform.
- `document_parser.py`: Handles the conversion of documents into text.
- `text_cleaner.py`: Cleans and preprocesses the extracted text.
- `tokenizer.py`: Tokenizes the text into manageable units.
- `lemmatizer.py`: Applies lemmatization to reduce words to their base forms.
- `metadata_extractor.py`: Extracts relevant metadata from the processed text.
- `output_formatter.py`: Formats the extracted metadata for output.
- `sample_invoice.pdf` & `sample_purchase_order.docx`: Sample documents for testing purposes.

## Contributing

Contributions are welcome! If you have suggestions for improvements or new features, please fork the repository and submit a pull request. For major changes, please open an issue first to discuss the proposed modifications.

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/YourFeature`)
3. Commit your Changes (`git commit -m 'Add YourFeature'`)
4. Push to the Branch (`git push origin feature/YourFeature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contact

For any questions or inquiries, please contact Akash Deore at [your-email@example.com].
