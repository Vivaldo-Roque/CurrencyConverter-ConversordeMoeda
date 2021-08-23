import os # Modulo referênte aos comandos do sistema
import requests # Modulo para solicitações HTTP
import json # Modulo responsável a manipulação de json
import socket # Modulo responsável por conexões
import sys #

#Função que verfica se tem internet ou não
def is_connected():
    try:
        socket.create_connection(("www.google.com", 80))
        return True
    except OSError:
        pass
    return False

#Está função tem a responsabilidade de pegar os cambios
def getCurrency():
    if(is_connected() == True):
        
        response = requests.get('https://www.freeforexapi.com/api/live?pairs=USDAOA,USDEUR,EURUSD') #Estou usando essa API grátis
        data = response.json()
        with open('data.json', 'w') as outfile:
            json.dump(data, outfile)
        exchange = [data["rates"]["USDAOA"]["rate"], data["rates"]["USDEUR"]["rate"]]
        return exchange
    
    elif(is_connected() == False):
        if os.path.exists("data.json") == True:
            with open('data.json') as json_file:
                data = json.load(json_file)
                exchange = [data["rates"]["USDAOA"]["rate"], data["rates"]["USDEUR"]["rate"]]
                return exchange
        else:
            sys.exit("Connecte a internet para baixar os dados!!!")

dados = getCurrency()
            
#como o nome já diz sobre a funções abaixo elas convertem
#AOA = Kwanza
#USD = Dollar
#EUR = Euro

def convertAOA_USD(valor,AOA):
    return round(valor * (1/AOA),2)

def convertUSD_AOA(valor,AOA):
    return round(valor * AOA,2)

def convertAOA_EUR(valor,EUR,AOA):
    return round(convertAOA_USD(valor,AOA) * EUR,2)

def convertEUR_AOA(valor,EUR,AOA):
    res = (1/EUR) * valor
    return round(convertUSD_AOA(res,AOA),2)

#Nota se não entendeste os calculos nas funções pesquise sobre: math currency conversion

#Essa função abaixo contém os texto dos menus
def info(x):

    if x == 1:

        print(
        " \n              B E M   V I N D O             "
        " \n| - - - - - - - - - - - - - - - - - - - - -|"
        " \nCONVERSAO DE KWANZA PARA MOEDAS INTERNACIONAS"
        " \n| - - - - - - - - - -||- - - - - - - - - - | "
        " \n|      M O E D A S   ||     V A L O R      | "
        " \n| - - - - - - - - - -||- - - - - - - - - - | "
        " \n| 1-  DOLAR <-> USD  ||    {0} AOA      | "
        " \n| 2-  EURO <-> EUR   ||    {1} AOA      | "
        " \n| - - - - - - - - - -||- - - - - - - - - - | \n"
        "\nDigite um numero para conversao a sua escolha ou 3 para sair do programa: ".format(round(dados[0],2),round(convertEUR_AOA(1,dados[1],dados[0]),2)))

    elif x == 2:

        print(
        "\n| - - - - - - - - - - - - - - - - - -|"
        "\n|        VOCE ESCOLHEU DOLAR         |"
        "\n| - - - - - - - - - - - - - - - - - -|"
        "\n| 1- CONVER. DE DOLAR PARA KWANZA    |"
        "\n| 2- CONVER. DE KWANZA PARA DOLAR    |\n"
        "\nDigte sua escolha de acordo com a tabela a cima ou 3 para sair do programa: ")

    elif x == 3:

        print(
        "\n| - - - - - - - - - - - - - - - - - |"
        "\n|        VOCE ESCOLHEU EURO         |"
        "\n| - - - - - - - - - - - - - - - - - |"
        "\n| 1- CONVER. DE EURO PARA KWANZA    |"
        "\n| 2- CONVER. DE KWANZA PARA EURO    |\n"
        "\nDigte sua escolha de acordo com a tabela a cima ou 3 para sair do programa: ")


os.system("color 1F")

while True:
    os.system("cls")
    print("Quer Converter?\n\"S\" ou \"N\"?")
    op = str(input("\t==> "))
    if op.lower() == "n":
        break
    elif op.lower() == "s":
        os.system("cls")
        info(1)
        escolha = int(input("\t==> "))
        os.system("cls")
        if escolha == 1:
            info(2)
            escolha = int(input("\t==> "))
            os.system("cls")
            if escolha == 1:
                print("\n - - - || DOLAR PARA KWANZA || - - -\n""\nDigite um valor em dolar = ")
                valor = float(input("\t==> "))
                print("\nIsso equivale a = {0} kz(AOA)\n".format(round(convertUSD_AOA(valor, dados[0]),2)))
            elif escolha == 2:
                print("\n - - - || KWANZA PARA DOLAR || - - -\n""\nDigite um valor em kwanza = ")
                valor = float(input("\t==> "))
                print("\nIsso equivale a = {0} dolares(USD)\n".format(round(convertAOA_USD(valor, dados[0]),2)))
            elif escolha == 3:
                break
            os.system("pause")	
        elif escolha == 2:
            info(3)
            escolha = int(input("\t==> "))
            os.system("cls")
            if escolha == 1:
                print("\n - - - || EURO PARA KWANZA || - - -\n""\nDigite um valor em euro = ")
                valor = float(input("\t==> "))
                print("\nIsso equivale a = {0} kz(AOA)\n".format(round(convertEUR_AOA(90.05,dados[1],dados[0]),2)))
            elif escolha == 2:
                    print("\n - - - || KWANZA PARA EUROS || - - -\n""\nDigite um valor em Kwanza = ")
                    valor = float(input("\t==> "))
                    print("\nIsso equivale a = {0} euros(EUR)\n".format(round(convertAOA_EUR(valor,dados[1],dados[0]),2)))
            elif escolha == 3:
                break
            os.system("pause")
        elif escolha == 3:
            break
        else:
            os.system("cls")
            print("opcao errada! tente novamente")
            os.system("pause")

os.system("cls")
print("\nO B R I G A D O  E  V O L T E  S E M P R E\n")
os.system("pause")
