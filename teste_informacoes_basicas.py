import unittest
from nessa_chatbot import *

class TesteInformacoesBasicas(unittest.TestCase):

    def setUp(self):
        self.robo = iniciar()

    def testar_o_que_e_programacao(self):
        perguntas = ["o que e programacao?"]

        for pergunta in perguntas:
            print(f"testando pergunta {pergunta}")

            resposta = self.robo.get_response(pergunta)
            self.assertGreaterEqual(resposta.confidence, CONFIANCA_MINIMA)
            self.assertIn(
                "Programação é o processo de criar e desenvolver programas de computador usando linguagens de programação. Envolve escrever um conjunto de instruções lógicas e algoritmos que guiam o computador na execução de tarefas específicas. Por meio da programação, os programadores podem criar software, aplicativos, sites e sistemas de computador, permitindo avanços tecnológicos e oferecendo oportunidades de carreira no campo da tecnologia da informação", 
                resposta.text
            )

    def testar_o_que_e_algoritmo(self):
        perguntas = ["o que é algoritmo?", "o que são algoritmos?"]

        for pergunta in perguntas:
            print(f"testando pergunta {pergunta}")

            resposta = self.robo.get_response(pergunta)
            self.assertGreaterEqual(resposta.confidence, CONFIANCA_MINIMA)
            self.assertIn(
                "Um algoritmo é uma sequência de passos lógicos e bem definidos que descrevem um processo ou solução para um problema. É uma abstração que permite aos programadores representar uma série de operações ou cálculos necessários para resolver uma determinada tarefa. Os algoritmos são independentes de linguagens de programação específicas e são usados para expressar a lógica e a sequência de ações que um programa deve seguir. Eles desempenham um papel fundamental na programação, pois fornecem a base para o desenvolvimento de software eficiente e soluções eficazes para uma variedade de problemas computacionais.", 
                resposta.text
            )

    def testar_o_que_e_linguagem_programacao(self):
        perguntas = ["o que é linguagem de programção?", "o que são linguagens de programação?", "o que é uma linguagem de programação?"]

        for pergunta in perguntas:
            print(f"testando pergunta {pergunta}")

            resposta = self.robo.get_response(pergunta)
            self.assertGreaterEqual(resposta.confidence, CONFIANCA_MINIMA)
            self.assertIn(
                "Uma linguagem de programação é uma forma padronizada de comunicação entre um programador e um computador. Ela consiste em um conjunto de regras, sintaxe e estruturas que permitem aos desenvolvedores escreverem programas de computador. As linguagens de programação fornecem um conjunto de instruções e comandos que podem ser compreendidos e executados pelo computador. Elas permitem que os programadores expressem suas ideias e lógica de forma estruturada, permitindo a criação de software, aplicativos, sites e sistemas. Cada linguagem de programação tem suas características e finalidades específicas, podendo ser de alto nível, como Python e Java, ou de baixo nível, como Assembly. As linguagens de programação são uma ferramenta essencial no desenvolvimento de soluções computacionais e desempenham um papel fundamental no avanço da tecnologia.", 
                resposta.text
            )

    def testar_o_que_e_python(self):
        perguntas = ["o que é python?"]

        for pergunta in perguntas:
            print(f"testando pergunta {pergunta}")

            resposta = self.robo.get_response(pergunta)
            self.assertGreaterEqual(resposta.confidence, CONFIANCA_MINIMA)
            self.assertIn(
                "Python é uma linguagem de programação de alto nível, interpretada e de propósito geral. Foi criada por Guido van Rossum e lançada pela primeira vez em 1991. Python é conhecida por sua sintaxe simples e legibilidade, o que a torna uma linguagem popular entre iniciantes e experientes em programação. Ela possui uma ampla variedade de usos, desde desenvolvimento de software, análise de dados e inteligência artificial até automação de tarefas e desenvolvimento web. Python é conhecida por sua filosofia 'batteries included', que significa que sua biblioteca padrão abrangente fornece muitas funcionalidades prontas para uso. Além disso, Python é uma linguagem de programação de código aberto e possui uma comunidade ativa que contribui com pacotes e frameworks adicionais, ampliando ainda mais suas capacidades.", 
                resposta.text
            )

    def testar_o_que_e_java(self):
        perguntas = ["o que é java?"]

        for pergunta in perguntas:
            print(f"testando pergunta {pergunta}")

            resposta = self.robo.get_response(pergunta)
            self.assertGreaterEqual(resposta.confidence, CONFIANCA_MINIMA)
            self.assertIn(
                "Java é uma linguagem de programação orientada a objetos, de propósito geral e amplamente utilizada. Ela foi desenvolvida pela Sun Microsystems e lançada em 1995. Java é conhecida por sua portabilidade, o que significa que os programas escritos em Java podem ser executados em diferentes sistemas operacionais sem a necessidade de alterações significativas. Ela é frequentemente usada para desenvolver aplicativos de software, aplicativos móveis, sistemas em tempo real, jogos e muito mais. Uma das principais características do Java é sua máquina virtual Java (JVM), que permite a execução do código Java em diferentes plataformas. Além disso, Java possui uma biblioteca padrão rica e uma comunidade ativa que contribui com uma ampla gama de frameworks e bibliotecas adicionais para facilitar o desenvolvimento de aplicativos complexos.", 
                resposta.text
            )

    def testar_o_que_e_cpp(self):
        perguntas = ["o que é c++?"]

        for pergunta in perguntas:
            print(f"testando pergunta {pergunta}")

            resposta = self.robo.get_response(pergunta)
            self.assertGreaterEqual(resposta.confidence, CONFIANCA_MINIMA)
            self.assertIn(
                "Java é uma linguagem de programação orientada a objetos, de propósito geral e amplamente utilizada. Ela foi desenvolvida pela Sun Microsystems e lançada em 1995. Java é conhecida por sua portabilidade, o que significa que os programas escritos em Java podem ser executados em diferentes sistemas operacionais sem a necessidade de alterações significativas. Ela é frequentemente usada para desenvolver aplicativos de software, aplicativos móveis, sistemas em tempo real, jogos e muito mais. Uma das principais características do Java é sua máquina virtual Java (JVM), que permite a execução do código Java em diferentes plataformas. Além disso, Java possui uma biblioteca padrão rica e uma comunidade ativa que contribui com uma ampla gama de frameworks e bibliotecas adicionais para facilitar o desenvolvimento de aplicativos complexos.",
                resposta.text
            )

    def testar_o_que_e_poo(self):
        perguntas = ["o que é orientacão a objeto?", "o que é programação orientada a objeto?"]

        for pergunta in perguntas:
            print(f"testando pergunta {pergunta}")

            resposta = self.robo.get_response(pergunta)
            self.assertGreaterEqual(resposta.confidence, CONFIANCA_MINIMA)
            self.assertIn(
                "A programação orientada a objetos (POO) é um paradigma de programação que se baseia na organização e estruturação do código em torno de objetos, que são instâncias de classes. Na POO, os objetos são criados a partir de modelos chamados classes, que definem seus atributos (dados) e métodos (comportamentos). Essa abordagem permite a reutilização de código, modularidade, encapsulamento e facilita a compreensão e manutenção do software. A POO se baseia em quatro princípios fundamentais: encapsulamento, herança, polimorfismo e abstração. O encapsulamento garante que os detalhes internos dos objetos sejam ocultados, permitindo apenas o acesso controlado aos dados e métodos relevantes. A herança permite que as classes herdem características e comportamentos de outras classes, estabelecendo uma relação hierárquica entre elas. O polimorfismo permite que objetos de diferentes classes respondam de maneira diferente ao mesmo método. A abstração permite que as classes sejam abstraídas de seus detalhes internos, fornecendo uma visão simplificada e focada nos aspectos essenciais. A POO é amplamente utilizada no desenvolvimento de software e fornece uma estrutura sólida e modular para criar aplicativos complexos e escaláveis.",
                resposta.text
            )

    def testar_o_que_sao_paradigmas_programacao(self):
        perguntas = ["o que são paradigmas de programação?"]

        for pergunta in perguntas:
            print(f"testando pergunta {pergunta}")

            resposta = self.robo.get_response(pergunta)
            self.assertGreaterEqual(resposta.confidence, CONFIANCA_MINIMA)
            self.assertIn(
                "Paradigmas de programação são abordagens ou estilos diferentes de organizar e estruturar o código de um programa. Cada paradigma possui um conjunto de conceitos, princípios e técnicas que guiam a forma como os programas são escritos e resolvem problemas computacionais. Alguns dos paradigmas mais comuns são: programação procedural, onde o programa é organizado em uma sequência de procedimentos ou funções; programação orientada a objetos, que organiza o código em torno de objetos, com atributos e comportamentos; programação funcional, que enfatiza o uso de funções puras e imutabilidade de dados; programação lógica, que se baseia na lógica formal e em regras de inferência; e programação estruturada, que utiliza estruturas de controle para criar programas mais claros e legíveis. Cada paradigma tem suas vantagens e desvantagens, e a escolha do paradigma certo depende do problema a ser resolvido, dos requisitos do projeto e das preferências pessoais do programador. Além disso, é comum a combinação de paradigmas para aproveitar o melhor de cada abordagem em um determinado contexto.",
                resposta.text
            )

    def testar_o_que_e_abstracao(self):
        perguntas = ["o que é abstração"]

        for pergunta in perguntas:
            print(f"testando pergunta {pergunta}")

            resposta = self.robo.get_response(pergunta)
            self.assertGreaterEqual(resposta.confidence, CONFIANCA_MINIMA)
            self.assertIn(
                "Abstração, na programação, é o processo de simplificar um sistema complexo, representando apenas os aspectos relevantes e ocultando os detalhes desnecessários. É uma técnica que permite criar modelos conceituais ou classes que representam objetos do mundo real, concentrando-se apenas nas características essenciais e ignorando a implementação interna. A abstração facilita a compreensão, a reutilização e a manutenção do código, fornecendo uma visão mais clara e focada nos aspectos-chave do sistema.",
                resposta.text
            )
    
if __name__ == "__main__":
    carregador = unittest.TestLoader()
    testes = unittest.TestSuite()

    testes.addTest(carregador.loadTestsFromTestCase(TesteInformacoesBasicas))

    executor = unittest.TextTestRunner()
    executor.run(testes)