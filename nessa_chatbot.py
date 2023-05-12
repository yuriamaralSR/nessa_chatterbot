from chatterbot import ChatBot

CONFIANCA_MINIMA = 0.70

def iniciar():
    robo = ChatBot("Nessa Chatbot",
        read_only = True,
        logic_adapters = [
            {
                "import_path": "chatterbot.logic.BestMatch"
            }
        ])

    return robo

def executar_robo(robo):
    while True:
        entrada = input("Digite alguma coisa... \n")
        resposta = robo.get_response(entrada.lower())
        if resposta.confidence >= CONFIANCA_MINIMA:
            print(">>", resposta.text)
        else:
            print("Infelizmente, ainda não sei responder isso")
            print("Pergunte outra coisa")

if __name__ == "__main__":
    robo = iniciar()

    executar_robo(robo)