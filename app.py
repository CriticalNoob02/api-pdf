from Reader import transcribe
from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/read', methods=['POST'])
def extractPDFs():
    # Recebendo o arquivo da requisição;
    pdf_file = request.files['pdf_file']
    
    # saalvando PDF recebido;
    pdf_file.save('./PDFs/file.pdf')

    # Função de leitura e escrita;
    text = transcribe('./PDFs/file.pdf')

    # Resposta enviada em formato JSON;
    return jsonify(text)

@app.route('/ocr', methods=['POST'])
def analizePDFs():
    return 


app.run(port=5000, host='localhost', debug=True)