import PyPDF2

def transcribe(url):
    pdf = open(url, 'rb')
    pdfleitura = PyPDF2.PdfReader(pdf)
    page = pdfleitura.pages[0]
    text = page.extract_text()
    return text