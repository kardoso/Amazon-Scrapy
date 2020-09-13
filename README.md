Este programa busca por uma palavra-chave no site da amazon, especificamente pela palavra "iphone", copia todos os resultados da primeira página e salva em um arquivo excel.

## Instalar requerimentos
Para instalar os requerimentos necessários para a aplicação execute no terminal o comando `pip install -r requirements.txt` (Python 2), ou `pip3 install -r requirements.txt` (Python 3) dentro do diretório com o arquivo `requirements.txt`.


### Executar a aplicação
Após ter instalado os requerimentos, execute o comando abaixo para executar a aplicação:

`scrapy crawl amazon_spider`

Esse comando irá gerar um arquivo excel chamado `produtos.xls` na pasta, contendo nomes e preços dos produtos da primeira página de busca.