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
    
    os.remove(url)

# Dividindo imagem;
def cutImg(url):
    img = cv2.imread(url)

    # Recuperando informação do tamanho da imagem;
    row, col, _ = img.shape

    # Removendo cores da imagem;
    imgGray = cv2.cvtColor (img,cv2.COLOR_BGR2GRAY)

    if row > 1000:
        # Cortando imagem na vertical;
        cut = round(row/3)

        imgCut1 = imgGray[0:cut, 0:col]
        imgCut2 = imgGray[cut:(cut*2), 0:col]
        imgCut3 = imgGray[(cut*2):(cut*3), 0:col]

        cv2.imwrite(f"./cut/cut_img1.png" ,imgCut1)
        cv2.imwrite(f"./cut/cut_img2.png" ,imgCut2)
        cv2.imwrite(f"./cut/cut_img3.png" ,imgCut3)

    elif col > 1000:
        # Cortando imagem na horizontal;
        cut = round(col/3)

        imgCut1 = imgGray[0:row, 0:cut]
        imgCut2 = imgGray[0:row, cut:(cut*2)]
        imgCut3 = imgGray[0:row, (cut*2):(cut*3)]

        cv2.imwrite(f"./cut/cut_img1.png" ,imgCut1)
        cv2.imwrite(f"./cut/cut_img2.png" ,imgCut2)
        cv2.imwrite(f"./cut/cut_img3.png" ,imgCut3)

# Faz a leitura e escrita da Imagem;
def readImg(url):
    img = cv2.imread(url)
    text = pytesseract.image_to_string(img)
    return text

# -=-=-=-= Função que engloba os Passos;
def ocr(file):
    changeFormat(file)

    # Criando array para o texto lido;
    array = []

    # Criando um loop com a quantidade de arquivos na pasta {imgs};
    path = './imgs'
    for root, dirs, files in os.walk(path):
        for i in range(len(files)):
            img = cv2.imread(f'./imgs/{files[i]}')

            # Recuperando informação do tamanho da imagem;
            row, col, _ = img.shape

            # Cortar a imagem caso seja grande;
            if row or col >= 1000:
                cutImg(f'./imgs/{files[i]}')

            # Loop para percorrer a pasta cut;
            for root2, dirs2, files2 in os.walk('./cut'):
                if len(files2) == 3:
                     for i in len(files2):
                        array.append(readImg(f'./cut/{files2[i]}'))
                        os.remove(f'./cut/{files2[i]}')
                else:
                   array.append(readImg(f'./imgs/{files[i]}')) 
                   os.remove(f'./imgs/{files[i]}')
    
    return array