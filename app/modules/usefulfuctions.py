import os
import socket # Module responsible for connections / Modulo responsável por conexões
import json # Module responsible for handling json / Modulo responsável a manipulação de json
import locale
import main

# Note: Only support EN, PT / Nota: Apenas suporta EN, PT
# Function to load languagues / Função que carrega as linguages
def loadLanguage():
    if os.path.exists(main.mydir+"/app/languages.json") == True:
        with open(main.mydir+'/app/languages.json') as json_file:
            data = json.load(json_file)
            systemLang = locale.getdefaultlocale()[0][:2]
        return data[systemLang]
    else:
        return None

# Function that checks if you have internet or not / Função que verifica se tem internet ou não
def is_connected():
    try:
        socket.create_connection(("www.google.com", 80))
        return True
    except OSError:
        pass
    return False

