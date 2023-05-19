import unittest
from nessa_chatbot import *

class TesteComandosDeBusca(unittest.TestCase):

    def setUp(self):
        self.robo = iniciar()

    def testar_busca_sobre(self):
        perguntas = ["gostaria de saber sobre uma coisa", "quero saber sobre uma coisa", "pesquise pra mim sobre", "me explique", "quero saber uma coisa"]

        for pergunta in perguntas:
            print(f"testando pergunta {pergunta}")

            resposta = self.robo.get_response(pergunta)

            executou = selecionar_comando(resposta)
            self.assertGreaterEqual(resposta.confidence, CONFIANCA_MINIMA)
            self.assertIn(
                "sobre", 
                resposta.text
            )
            self.assertTrue(executou)


    def testar_busca_exercicio(self):
        perguntas = ["exercício", "exercícios", "gostaria de um exercício", "queria um exercício", "me traga um exercío", "encontre um exercício para mim"]

        for pergunta in perguntas:
            print(f"testando pergunta {pergunta}")

            resposta = self.robo.get_response(pergunta)

            executou = selecionar_comando(resposta)
            self.assertGreaterEqual(resposta.confidence, CONFIANCA_MINIMA)
            self.assertIn(
                "exercicio", 
                resposta.text
            )
            self.assertTrue(executou)

    def testar_busca_video(self):
        perguntas = ["vídeo", "vídeos", "gostaria de ver um vídeo", "queria um vídeo", "me traga um vídeo", "encontre um vídeo para mim"]

        for pergunta in perguntas:
            print(f"testando pergunta {pergunta}")

            resposta = self.robo.get_response(pergunta)

            executou = selecionar_comando(resposta)
            self.assertGreaterEqual(resposta.confidence, CONFIANCA_MINIMA)
            self.assertIn(
                "video", 
                resposta.text
            )
            self.assertTrue(executou)

    def testar_busca_tutorial(self):
        perguntas = ["tutorial", "tutoriais", "gostaria de ver um tutorial", "queria um tutorial", "me traga um tutorial", "encontre um tutorial para mim"]

        for pergunta in perguntas:
            print(f"testando pergunta {pergunta}")

            resposta = self.robo.get_response(pergunta)

            executou = selecionar_comando(resposta)
            self.assertGreaterEqual(resposta.confidence, CONFIANCA_MINIMA)
            self.assertIn(
                "tutorial", 
                resposta.text
            )
            self.assertTrue(executou)
    
if __name__ == "__main__":
    carregador = unittest.TestLoader()
    testes = unittest.TestSuite()

    testes.addTest(carregador.loadTestsFromTestCase(TesteComandosDeBusca))

    executor = unittest.TextTestRunner()
    executor.run(testes)