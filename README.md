# Conecta Distribuição: Bot para Informações de Distribuição da FEMSA Coca-Cola no WhatsApp

## Descrição

O Conecta Distribuição é um bot para WhatsApp que fornece informações sobre o status de pedidos da FEMSA Coca-Cola de forma rápida e fácil. Com ele, clientes e vendedores podem:

*   Consultar o status de seus pedidos (em rota, pendente ou suspenso).
*   Vendedores têm acesso a informações detalhadas sobre os pedidos, como:
    *   Placa do caminhão.
    *   Transportadora.
    *   Contato da transportadora.

## Funcionalidades

### Consulta de Status do Pedido

Basta digitar a matrícula do pedido para receber informações atualizadas sobre o status.

### Opções para Vendedores

Vendedores podem digitar "opções" para acessar as informações detalhadas sobre os pedidos.

## Como usar

1.  Acesse o WhatsApp e envie uma mensagem para o número do bot.
2.  Para consultar o status de um pedido, digite a matrícula do pedido.
3.  Vendedores podem digitar "opções" para acessar as opções extras.

## Tecnologias utilizadas

*   Python
*   Flask
*   Twilio
*   Pandas

## Instalação

1.  Clone este repositório: `git clone https://github.com/GustavoLibano/ConectaDistribuicao.git`
2.  Instale as dependências: `pip install -r requirements.txt`
3.  Crie um arquivo `.env` e adicione as suas credenciais Twilio e o caminho para a planilha:

    ```
    ACCOUNT_SID=SEU_ACCOUNT_SID
    AUTH_TOKEN=SEU_AUTH_TOKEN
    PLANILHA_PATH=caminho/para/sua/planilha.xlsx
    ```

4.  Execute o bot: `python app.py`

## Contribuição

Sinta-se à vontade para contribuir com este projeto! Se você tiver alguma sugestão, ideia ou correção, abra uma issue ou envie um pull request.

## Licença

Este projeto está sob a licença MIT.

## Contato

Se você tiver alguma dúvida ou sugestão, entre em contato: [gustavolleandro@outlook.com]

---
