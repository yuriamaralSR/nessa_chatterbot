import unittest
from nessa_chatbot import *

class TesteSaudacoes(unittest.TestCase):

    def setUp(self):
        self.robo = iniciar()

    def testar_oi_ola_eai(self):
        saudacoes = ["oi", "olá", "eai"]

        for saudacao in saudacoes:
            print(f"testando saudação {saudacao}")

            resposta = self.robo.get_response(saudacao)
            self.assertGreaterEqual(resposta.confidence, CONFIANCA_MINIMA)
            self.assertIn(
                "Olá, sou o robô de atendimento Nessa e estou aqui para te auxiliar em seus estudos de programação. Como posso ajudar?", 
                resposta.text
            )

    def testar_bom_dia_boa_tarde_boa_noite(self):
        saudacoes = ["Bom dia", "Boa tarde", "Boa noite"]

        for saudacao in saudacoes:
            print(f"testando saudação {saudacao}")

            resposta = self.robo.get_response(saudacao.lower())
            self.assertGreaterEqual(resposta.confidence, CONFIANCA_MINIMA)
            self.assertIn(
                saudacao + ", sou o robô de atendimento Nessa e estou aqui para te auxiliar em seus estudos de programação. Como posso ajudar?",
                resposta.text
            )

    def testar_tem_alguem_ai(self):
        saudacoes = ["tem alguem ai?"]

        for saudacao in saudacoes:
            print(f"testando saudação {saudacao}")

            resposta = self.robo.get_response(saudacao.lower())
            self.assertGreaterEqual(resposta.confidence, CONFIANCA_MINIMA)
            self.assertIn(
                "Tem sim. Eu sou a Nessa, um robô de atendimento e estou aqui para te auxiliar em seus estudos de programação. Como posso ajudar?",
                resposta.text
            )

    def testar_oi_ola_eai_nessa(self):
        saudacoes = ["oi nessa", "ola nessa", "eai nessa"]

        for saudacao in saudacoes:
            print(f"testando saudação {saudacao}")

            resposta = self.robo.get_response(saudacao.lower())
            self.assertGreaterEqual(resposta.confidence, CONFIANCA_MINIMA)
            self.assertIn(
                "Olá, tudo bem? Como posso ajudar?",
                resposta.text
            )

    def testar_variabilidades_saudacoes(self):
        saudacoes = [ "Bom dia", "Boa tarde", "Boa noite" ]

        for saudacao in saudacoes:
            print(f"testando saudação {saudacao}")

            resposta = self.robo.get_response("oi, " + saudacao.lower())
            self.assertGreaterEqual(resposta.confidence, CONFIANCA_MINIMA)
            self.assertIn(
                saudacao + ", sou o robô de atendimento Nessa e estou aqui para te auxiliar em seus estudos de programação. Como posso ajudar?",
                resposta.text
            )

if __name__ == "__main__":
    carregador = unittest.TestLoader()
    testes = unittest.TestSuite()

    testes.addTest(carregador.loadTestsFromTestCase(TesteSaudacoes))

    executor = unittest.TextTestRunner()
    executor.run(testes)