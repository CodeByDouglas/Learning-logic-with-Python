import backend.verificadores
import json
import os


bancodepessoas={
    "Alice": 30,
    "Bruno": 25,
    "Carla": 28,
    "Daniel": 35,
    "Eduardo": 40,
    "Fernanda": 22,
    "Gustavo": 27,
    "Helena": 33,
    "Igor": 29,
    "Julia": 24
    }

def carregar_BDD():
    global bancodepessoas
    localdoarquivo=os.path.join('ex115','Dados','SaveDados')
    if os.path.exists(localdoarquivo):
        with open(localdoarquivo, "r") as saveBDD:
            bancodepessoas=json.load(saveBDD)
    else:
        with open(localdoarquivo, "w") as saveBDD:
            json.dump(bancodepessoas,saveBDD)



def cadastrar_pessoa():
    localdoarquivo=os.path.join('ex115','Dados','SaveDados')
    global bancodepessoas
    Nome=backend.verificadores.valid_str('Insira o nome da pessoa: ')
    Idade=backend.verificadores.valid_int('Insira a idade da pessoa: ')
    bancodepessoas[Nome]=Idade
    with open(localdoarquivo,"w") as saveBDD:
        json.dump(bancodepessoas,saveBDD)
    


def exibir_pessoas():
    global bancodepessoas
    
    for x, y in bancodepessoas.items():
        print(f'{x:<20}{y} anos')