PDF Text Extractor with Handwritten Notes

This Python project extracts typed text and handwritten notes from a PDF and saves it to a .txt file. It uses Tesseract OCR to detect handwritten text from the PDF pages (which are converted to images).
Table of Contents

    Requirements
    Installation
    Usage
    Known Issues
    License

Requirements

    Python 3.x
    Libraries: PyPDF2, pdfplumber, pytesseract, Pillow, pdf2image
    Tesseract OCR (for handwritten text extraction)

Installation
1. Clone the Repository

Clone this repository to your local machine:

bash

git clone https://github.com/your-username/pdf-text-extractor.git
cd pdf-text-extractor

2. Install Python Libraries

Use pip to install the necessary Python libraries:

bash

pip install PyPDF2 pdfplumber pytesseract Pillow pdf2image

3. Install Tesseract OCR
Windows

    Download the Tesseract installer from Tesseract GitHub Releases and run it.
    After installation, add the Tesseract executable to your system's PATH:
        Open System Properties → Environment Variables.
        Find the PATH variable and click Edit.
        Add the directory where Tesseract is installed (e.g., C:\Program Files\Tesseract-OCR).
    Verify the installation by running:

    bash

    tesseract --version

Linux

    Install Tesseract using the package manager:

    bash

sudo apt-get update
sudo apt-get install tesseract-ocr

Verify the installation by running:

bash

    tesseract --version

4. Configure pdf2image (Linux only)

To use pdf2image on Linux, you need to install poppler-utils:

bash

sudo apt-get install poppler-utils

Usage

    Place your PDF file in the project directory.

    Update the paths to your PDF file and the output text file in the Python script:

    python

pdf_file_path = 'your_pdf_with_handwritten_notes.pdf'
output_file_path = 'extracted_text.txt'

Run the script:

bash

python extract_pdf_text.py

After the script finishes, the extracted text (both typed and handwritten) will be saved to the specified .txt file.

P.S:

Handwritten text accuracy: The OCR accuracy depends on the clarity and legibility of the handwriting in the PDF. Poor-quality handwriting may not be recognized well by Tesseract.
Large PDFs: Processing large PDFs with many pages might take time and consume a lot of memory.