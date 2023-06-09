import json
from chatterbot  import ChatBot
from chatterbot.trainers import ListTrainer

CONVERSAS = [
    "conversas/saudacoes.json",
    "conversas/informacoes_basicas.json",
    "conversas/comandos_de_busca.json",
    "conversas/comandos_abrir.json"
]

def iniciar():
    robo = ChatBot("Nessa Chatbot")
    treinador = ListTrainer(robo)

    return treinador

def carregar_conversas():
    conversas = []

    for arquivos_de_conversas in CONVERSAS:
        with open(arquivos_de_conversas, "r", encoding="utf-8") as arquivo:
            conversas_treinamento = json.load(arquivo)
            conversas.append(conversas_treinamento["conversas"])

            arquivo.close()

    return conversas

def treinar(treinador, conversas):
    for conversa in conversas:
        for perguntas_resposta in conversa:
            perguntas = perguntas_resposta["perguntas"]
            resposta = perguntas_resposta["resposta"]

            print(f"Treinando o robô... // Perguntas: {perguntas}. Resposta: {resposta}")
            for pergunta in perguntas:
                treinador.train([pergunta, resposta])

if __name__ == "__main__":
    treinador = iniciar()

    conversas = carregar_conversas()
    if conversas:
        treinar(treinador, conversas)
