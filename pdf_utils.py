from PyPDF2 import PdfReader
from langchain.text_splitter import RecursiveCharacterTextSplitter
import logging

def read_pdf(uploaded_file):
    """
    Read the content of the uploaded PDF file and return the extracted text.
    """
    try:
        pdf_reader = PdfReader(uploaded_file)
        text = ""
        for page in pdf_reader.pages:
            text += page.extract_text()
        if not text.strip():
            logging.warning("Extracted text is empty")
        return text
    except Exception as e:
        logging.error(f"Error reading PDF: {str(e)}")
        return ""

def split_text(text, chunk_size=1000, chunk_overlap=200):
    """
    Split the input text into chunks using RecursiveCharacterTextSplitter.
    """
    if not text.strip():
        logging.warning("Input text is empty, cannot split")
        return []
    
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=chunk_size,
        chunk_overlap=chunk_overlap,
        length_function=len
    )
    return text_splitter.split_text(text)
