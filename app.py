from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse
import pandas as pd

app = Flask(__name__)
account_sid = ""
auth_token = ""
planilha_path = r""

@app.route("/whatsapp", methods=["POST"])
def whatsapp():
    mensagem = request.form.get("Body").lower()
    resposta = MessagingResponse()
    try:
        df = pd.read_excel(planilha_path)
        if mensagem == "listar pedidos":
            pedidos = df[["Matrícula", "Placa do Caminhão", "Transportadora"]].to_string(index=False)
            resposta.message(f"Lista de pedidos:\n{pedidos}")
        elif mensagem.isdigit():
            matricula = int(mensagem)
            pedido = df[df["Matrícula"] == matricula]
            if not pedido.empty:
                status = pedido["Status do Pedido"].iloc[0]
                placa = pedido["Placa do Caminhão"].iloc[0]
                transportadora = pedido["Transportadora"].iloc[0]
                resposta.message(
                    f"Seu pedido está {status} na placa {placa}, da transportadora {transportadora}."
                )
            else:
                resposta.message("Matrícula não encontrada. Por favor, digite uma matrícula válida.")
        elif "opções" in mensagem:
            resposta.message(
                "Opções:\n"
                "- Qual placa está o pedido [Matrícula]?\n"
                "- Qual a transportadora do pedido [Matrícula]?\n"
                "- Contato da transportadora do pedido [Matrícula]"
            )
        elif "placa" in mensagem and any(digit in mensagem for digit in "1234567890"):
            matricula = int("".join(filter(str.isdigit, mensagem)))
            pedido = df[df["Matrícula"] == matricula]
            if not pedido.empty:
                placa = pedido["Placa do Caminhão"].iloc[0]
                resposta.message(f"A placa do pedido {matricula} é {placa}.")
            else:
                resposta.message("Matrícula não encontrada. Por favor, digite uma matrícula válida.")
        elif "transportadora" in mensagem and any(digit in mensagem for digit in "1234567890"):
            matricula = int("".join(filter(str.isdigit, mensagem)))
            pedido = df[df["Matrícula"] == matricula]
            if not pedido.empty:
                transportadora = pedido["Transportadora"].iloc[0]
                resposta.message(f"A transportadora do pedido {matricula} é {transportadora}.")
            else:
                resposta.message("Matrícula não encontrada. Por favor, digite uma matrícula válida.")
        elif "contato" in mensagem and any(digit in mensagem for digit in "1234567890"):
            matricula = int("".join(filter(str.isdigit, mensagem)))
            pedido = df[df["Matrícula"] == matricula]
            if not pedido.empty:
                transportadora = pedido["Transportadora"].iloc[0]
                resposta.message(f"O contato da transportadora {transportadora} é [Contato].")
            else:
                resposta.message("Matrícula não encontrada. Por favor, digite uma matrícula válida.")
        else:
            resposta.message("Por favor, digite sua matrícula, 'listar pedidos' ou uma das opções para vendedores.")
    except Exception as e:
        resposta.message("Ocorreu um erro. Por favor, tente novamente mais tarde.")
        print(f"Erro: {e}")
    return str(resposta)

if __name__ == "__main__":
    app.run(debug=True)