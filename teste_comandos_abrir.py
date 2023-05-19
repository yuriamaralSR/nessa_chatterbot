import unittest
from nessa_chatbot import *

class TesteComandosAbrir(unittest.TestCase):

    def setUp(self):
        self.robo = iniciar()

    def testar_abrir_doc_python(self):
        perguntas = ["doc python", "documentação python", "documentação do python", "abra a documentação do python", "abra pra mim a documentação do python"]

        for pergunta in perguntas:
            print(f"testando pergunta {pergunta}")

            resposta = self.robo.get_response(pergunta)

            executou = selecionar_comando(resposta)
            self.assertGreaterEqual(resposta.confidence, CONFIANCA_MINIMA)
            self.assertIn(
                "doc_python", 
                resposta.text
            )
            self.assertTrue(executou)


    def testar_abrir_doc_java(self):
        perguntas = ["doc java", "documentação java", "documentação do java", "abra a documentação do java", "abra pra mim a documentação do java"]

        for pergunta in perguntas:
            print(f"testando pergunta {pergunta}")

            resposta = self.robo.get_response(pergunta)

            executou = selecionar_comando(resposta)
            self.assertGreaterEqual(resposta.confidence, CONFIANCA_MINIMA)
            self.assertIn(
                "doc_java", 
                resposta.text
            )
            self.assertTrue(executou)

    def testar_abrir_doc_cpp(self):
        perguntas = ["doc c++", "documentação c++", "documentação do c++", "abra a documentação do c++", "abra pra mim a documentação do c++"]

        for pergunta in perguntas:
            print(f"testando pergunta {pergunta}")

            resposta = self.robo.get_response(pergunta)

            executou = selecionar_comando(resposta)
            self.assertGreaterEqual(resposta.confidence, CONFIANCA_MINIMA)
            self.assertIn(
                "doc_c++", 
                resposta.text
            )
            self.assertTrue(executou)

    def testar_abir_vscode(self):
        perguntas = ["code", "quero codar", "vscode", "quero colocar a mão na massa", "visual studio code", "abra o vscode", "abra pra mim o vscode"]

        for pergunta in perguntas:
            print(f"testando pergunta {pergunta}")

            resposta = self.robo.get_response(pergunta)

            executou = selecionar_comando(resposta)
            self.assertGreaterEqual(resposta.confidence, CONFIANCA_MINIMA)
            self.assertIn(
                "vs_code", 
                resposta.text
            )
            self.assertTrue(executou)
    
if __name__ == "__main__":
    carregador = unittest.TestLoader()
    testes = unittest.TestSuite()

    testes.addTest(carregador.loadTestsFromTestCase(TesteComandosAbrir))

    executor = unittest.TextTestRunner()
    executor.run(testes)