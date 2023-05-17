import webbrowser
import wikipedia

def atuar_modulo_buscar(resposta, parametro):
    executou = False

    if resposta in ["sobre"]:
        if len(parametro) >= 1:
            parametros = " ".join(parametro)
            buscar_conceito(parametros)
            executou = True
        else:
            buscar_conceito(parametro)
            executou = True
    
    elif resposta in ["tutorial", "video"]:
        if len(parametro) >= 1:
            parametros = " ".join(parametro)
            buscar_tutorial(parametros)
            executou = True
        else:
            buscar_tutorial(parametro)
            executou = True
    elif resposta in ["exercicio"]:
        if len(parametro) >= 1:
            parametros = " ".join(parametro)
            buscar_exercicio(parametros)
            executou = True
        else:
            buscar_exercicio(parametro)
            executou = True

    return executou

def buscar_exercicio(parametros):
    url_exercicio = "https://google.com"
    webbrowser.get('windows-default').open_new(f'{url_exercicio}/search?q=exercício+{parametros}')

def buscar_tutorial(parametros):
    url_tutorial = "https://youtube.com"
    webbrowser.get('windows-default').open_new(f'{url_tutorial}/search?q={parametros}')

def buscar_conceito(parametro):
    wikipedia.set_lang('pt')
    try:
        print(wikipedia.summary(parametro))
        pagina = wikipedia.page(parametro)
        print(f"Veja mais em: {pagina.url}")
        
    except wikipedia.exceptions.DisambiguationError as e:
        print(f"Não foi possível encontrar uma definição precisa para '{parametro}'.")
        print("Por favor, tente especificar sua pesquisa com mais detalhes ou escolha um dos seguintes termos:")
        for i, termo in enumerate(e.options):
            print(f"{i + 1}. {termo}")