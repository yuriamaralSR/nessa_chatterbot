import webbrowser
import subprocess

def atuar_modulo_abrir(resposta, parametro):
    executou = False

    if resposta in ["doc_python", "doc_java", "doc_c++"]:
        if parametro == "java":
            webbrowser.get('windows-default').open_new("https://docs.oracle.com/en/java/")
            executou = True
        elif parametro == "python":
            webbrowser.get('windows-default').open_new("https://docs.python.org/3/")
            executou = True
        elif parametro == "c++":
            webbrowser.get('windows-default').open_new("https://pt.cppreference.com/w/")
            executou = True
        else:
            executou = False
    elif resposta == "vs_code":
        with subprocess.Popen(['cmd', '/c', 'start', 'code', '-n']):
            executou = True

    return executou