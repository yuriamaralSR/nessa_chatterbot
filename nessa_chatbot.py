from difflib import SequenceMatcher
from chatterbot import ChatBot
from unidecode import unidecode
from buscar import *

CONFIANCA_MINIMA = 0.70

def comparar_mensagens(mensagem_digitada, mensagem_candidata):
    confianca = 0.0

    digitada = mensagem_digitada.text
    candidata = mensagem_candidata.text
    if digitada and candidata:
        confianca = SequenceMatcher(
            None,
            digitada,
            candidata
        )
        confianca = round(confianca.ratio(), 2)

    return confianca

def selecionar_comando(resposta):
    executou = False
    
    if resposta == "sobre":
        parametro = input("Digite sobre o que quer saber: ")
        print("\n")
        parametro_dividido = parametro.split()
        executou = atuar_modulo_buscar(resposta, parametro_dividido)
        return executou
    if resposta == "exercicio":
        parametro = input("Digite o tema do exercício: ")
        parametro_dividido = parametro.split()
        executou = atuar_modulo_buscar(resposta, parametro_dividido)
        return executou
    if resposta in ("video", "tutorial"):
        parametro = input("Digite o tema do tutorial: ")
        parametro_dividido = parametro.split()
        executou = atuar_modulo_buscar(resposta, parametro_dividido)
        return executou
    if resposta == "doc_python":
        ...
    if resposta == "doc_java":
        ...
    if resposta == "doc_c++":
        ...
    if resposta == "vs_code":
        ...
    if resposta:
        return resposta        
    
    return print("Não encontrado. Tente novamente")

def iniciar():
    robo = ChatBot("Nessa Chatbot",
        read_only = True,
        statement_comparison_function=comparar_mensagens,
        logic_adapters = [
            {
                "import_path": "chatterbot.logic.BestMatch"
            }
        ])

    return robo

def executar_robo(robo):
    while True:
        entrada = input(">> ")
        entrada_unidecode = unidecode(entrada)
        resposta = robo.get_response(entrada_unidecode.lower())
        if resposta.confidence >= CONFIANCA_MINIMA:
            print(selecionar_comando(resposta.text))
        else:
            print("Infelizmente, ainda não sei responder isso")
            print("Pergunte outra coisa")

if __name__ == "__main__":
    robo = iniciar()

    executar_robo(robo)