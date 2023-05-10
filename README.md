# API de tratamento de dados:

Uma API que responsável por ler e repassar apenas as informações de texto de um pdf, utilizando duas formas de leitura: Leitura binária, Leitura por OCR;

Enviar o arquivo PDF dentro da requisição HTTP.

## Endpoints:

Leitor binário - Retorma os dados de texto do PDF;
{
    Texto
}

- `http://localhost:{PORT}/reader`

Leitor por OCR - Transforma o pdf em imagem e faz uma leitura do texto;
{
    Texto
} 

- `http://localhost:{PORT}/OCR`
 
## Atualizações 🎉:

- Ajustar melhor a edição da imagem para ajudar a leitura do OCR;
