import PyPDF2
import os

def transcribe(url):
    pdf = open(url, 'rb')
    pdfleitura = PyPDF2.PdfReader(pdf)
    page = pdfleitura.pages[0]
    text = page.extract_text()
    os.remove(url)
    return text