import PyPDF2
import pdfplumber
from pdf2image import convert_from_path
from PIL import Image
import pytesseract

# Path to the Tesseract executable (set this only if it's not in your PATH)
# pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

def extract_typed_text(pdf_file):
    typed_text = ""
    with pdfplumber.open(pdf_file) as pdf:
        for page in pdf.pages:
            typed_text += page.extract_text() + "\n"
    return typed_text

def extract_handwritten_text_from_images(pdf_file):
    # Convert PDF pages to images
    images = convert_from_path(pdf_file)
    handwritten_text = ""
    
    for i, image in enumerate(images):
        # Use Tesseract to extract text from each image
        text = pytesseract.image_to_string(image)
        handwritten_text += f"Page {i+1} Handwritten Text:\n{text}\n\n"
    
    return handwritten_text

def save_text_to_file(text, output_file):
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(text)

def extract_text_from_pdf(pdf_file, output_file):
    typed_text = extract_typed_text(pdf_file)
    
    handwritten_text = extract_handwritten_text_from_images(pdf_file)
    
    # Combine typed and handwritten text
    combined_text = "Typed Text:\n" + typed_text + "\nHandwritten Notes:\n" + handwritten_text
    
    # Save the extracted text to a txt file
    save_text_to_file(combined_text, output_file)
    print(f"Text successfully extracted and saved to {output_file}")

# Usage
pdf_file_path = r'./input.pdf'
output_file_path = 'extracted_text.txt'

extract_text_from_pdf(pdf_file_path, output_file_path)
