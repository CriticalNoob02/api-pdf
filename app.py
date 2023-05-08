from Reader import transcribe
from Ocr import ocr
from flask import Flask, jsonify, request, flash

app = Flask(__name__)

@app.route('/read', methods=['POST'])
def extractPDFs_reader():
    if not request.files:
        return jsonify('Infelizmente não recebi nenhum arquivo em PDF para ler...')
    
    else:
        # Recebendo o arquivo da requisição;
        pdf_file = request.files['pdf_file']
        
        # saalvando PDF recebido;
        pdf_file.save('./PDFs/file.pdf')

        # Função de leitura e escrita;
        text = transcribe('./PDFs/file.pdf')

        # Resposta enviada em formato JSON;
        return jsonify(text)

@app.route('/ocr', methods=['POST'])
def extractPDFs_ocr():
    if not request.files:
        return jsonify('Infelizmente não recebi nenhum arquivo em PDF para ler...')
    
    else:
            # Recebendo o arquivo da requisição;
        pdf_file = request.files['pdf_file']
        
        # saalvando PDF recebido;
        pdf_file.save('./PDFs/file.pdf')

        # Função de leitura e escrita;
        text = ocr('./PDFs/file.pdf')

        # Resposta enviada em formato JSON;
        return jsonify(text)


app.run(port=5000, host='localhost', debug=True)