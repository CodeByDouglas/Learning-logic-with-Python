# importando as funções criadas para o funcionamento do menu.
import backend.verificadores 
import backend.bancodedados 


# Função que carrega o arquivo Json com a lista de pessoas.
backend.bancodedados.carregar_BDD()
# Menu de opções 
while True:
        print(f'''
{30*'-'}
{'MENU PRINCIPAL'.center(30)}
{30*'-'}
1 - Ver pessoas cadastradas
2 - Cadastrar nova pessoa
3 - Sair do sistema
{30*'-'}''')
        opçao=backend.verificadores.valid_opção('Incira sua opção: ') # Utiliza uma ferramenta criada para verificar se o número é um número e se ele está entre 0 e 3.
        if opçao==1:
            backend.bancodedados.exibir_pessoas() # Chama a função que exibe as pessos cadastradas.
        elif opçao==2:
            backend.bancodedados.cadastrar_pessoa() # Chama a função que cadasta pessoas no arquivo json.
        elif opçao==3:
            print('Programa Finalizado volte sempre!') # Finaliza o programa.
            break