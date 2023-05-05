import pytesseract
import cv2
import fitz
import os

# -=-=-=-= Passos para a leitura;

# Muda o formato de PDF para PNG;
def changeFormat(url):
    doc = fitz.open(url) # type: ignore

    for i in range(doc.page_count):
        page = doc.load_page(i)
        pix = page.get_pixmap()
        pix.save(f"./imgs/{page.number}.png")

    for i in range(doc.page_count):
        page = doc.load_page(i)
        link = page.get_links()

# Ajusta as cores para melhorar a leitura;
def changeColor(url, name):
    # Gray transform;
    img = cv2.imread(url, cv2.IMREAD_GRAYSCALE)
    
    # DualColor transform;
    _, img2Color = cv2.threshold(img, 110, 245, cv2.THRESH_BINARY)
    cv2.imshow('img2Color', img2Color)

    # # Contours create;
    # contours, hier = cv2.findContours(img2Color, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)

    # # Contours aplly;
    # cv2.drawContours(img, contours, -1, (0, 255, 0), 2)
    # cv2.imshow("cont", img)

    # Save IMG;
    cv2.imwrite(f"./src/reader/imgs/{name}.png" ,img2Color)
    url2 = (f"./src/reader/imgs/{name}.png")
    
    return url2

# Faz a leitura e escrita da Imagem;
def readImg(url):
    img = cv2.imread(url)
    text = pytesseract.image_to_string(img)
    print(text)

# -=-=-=-= Função que engloba os Passos;
def aaa(file):
    changeFormat(file)

    # Criando um loop com a quantidade de arquivos na pasta {imgs};
    path = './imgs'
    for root, dirs, files in os.walk(path):
        for i in range(len(files)):
            print(files[i])


aaa('./PDFs/file.pdf')







# path = './cypress/downloads'

# for root, dirs, files in os.walk(path):
#     for i in range(len(files)):
#         market = root.split('/')
#         url = (os.path.join(os.path.realpath(root), files[i]))
#         print(os.path.join(os.path.realpath(root), files[i]))
#         name = f'{market[-1]}/Palhoça'
#         id = i

#         changeFormat(url, name, id)