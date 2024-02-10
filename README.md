# NWL Python Project

Projeto desenvolvido em Python durante o 14ª NLW Expert Ofertado pela Rockseat. Trata-se de um gerador de Código de Barras embasado em padrões de projeto, bibliotecas e responsabilidades definidas

# :hammer: Funcionalidades do Projeto

- `Função`: Receber um código em formato String via API e gerar uma imagem contendo um Código de Barras no padrão 128
- `Utilização de bibliotecas`: Através de um servidor Web, disponibilizado na porta 3000 e criado com o Flask, o endpoint /create_tag receberá através do metodo POST um JSON contendo a chave "product_code" com uma string que será gerado um código de barras com a biblioteca python-barcode e por sua vez o pillow irá gerar e salvar uma imagen contendo esse código de barras. Para garantir a documentação e padronização do código foi utilizado o Pylint e o pre-commit para garantir que as regras foram atendidas antes mesmo de enviar o código para o repositório git. Para realizar a validação dos dados foi utilizado o Cerberus, que provê uma vasta gama de validações dos dados recebidos pelo endpoint e caso algum dado não estivesse de acordo com as regras seria informado em uma resposta amigável e direcionada ao erro. Também foi utilizado neste projeto o pytest para garantir a continuidade do projeto mantendo o funcionamento adequado das funções, através de testes unitários é possível que rapidamente todo o código seja revisto/retestado sem novo esforço de desenvolvimento.



# :heavy_check_mark: Tecnologias e Dependências
* Python 3.12
* Pylint
* pre-commit 
* Flask
* python-barcode
* pillow
* cerberus
* pytest


# :mechanical_arm: Como executar
* Python 3.12 instalado
* Postman ou Insomnia instalado
* Download do repositório
* Abra o terminal e acesse a pasta do projeto
* execute o seguinte comando: python run.py
    * O servidor flask estará disponível em localhost na porta 3000
* Para testar, abra o postman por exemplo, crie uma requisição POST com a url http://localhost:3000/create_tag
    * No body da requisição é preciso selecionar raw e então JSON para definir os parâmetros que serão enviados pela requisição
    * O Json será construído desta forma: 

{
    "product_code": "12R85J5d"
}

* A resposta do servidor será em formato JSON confirmado a criação da Imagem com o Código de Barras:
    * count: exibe a quantidade de imagens criadas, neste endpoint cria uma única imagem.
    * path: apresenta o nome e o formato da imagem criada
    * type: "Tag Image" informa que a imagem é do tipo Tag, neste endpoint contém somente este tipo.

{
  "data": {
    "count": 1,
    "path": "12R85J5d.png",
    "type": "Tag Image"
  }
}

* Por exemplo, em caso de envio de uma requisição incorreta, ao invés de enviar um código em formato string foi enviado um inteiro:

{
    "product_code": 6688
}

* A resposta do servidor será a seguinte:
    * Ocorreu um erro, apontando que a chave "product_code" deve receber um parâmetro do tipo string. Esta resposta foi estruturada com o auxílio da biblioteca Cerberus.
{
    "errors": [
        {
            "detail": {
                "product_code": [
                    "must be of string type"
                ]
            },
            "title": "UnprocessableEntity"
        }
    ]
}

![Badge em Desenvolvimento](http://img.shields.io/static/v1?label=dEV&message=PYTHON&color=GREEN&style=for-the-badge)