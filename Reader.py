import PyPDF2
import os

def transcribe(url):
    # Abrindo arquivo em formato binário;
    pdf = open(url, 'rb')

    # Leitor do PDF;
    readerPDF = PyPDF2.PdfReader(pdf)
    text = []

    # Loop pelas páginas do PDF;
    for i in len(readerPDF.pages):
        page = readerPDF.pages[i]

        # Extração do texto;
        text.append(page.extract_text())

    # Limpando arquivos já usados
    os.remove(url)
    return text