from datetime import datetime

cadastro={}
cadastro['nome']=str(input('Qual o nome do user: '))
anodenascimento=int(input('Qual ano do seu nascimento: '))
cadastro['cdt']=int(input('Insira os número da sua carteira de trabalho(Caso não ouver digite 0): '))
cadastro['idade']=datetime.now().year - anodenascimento

if cadastro['cdt']!=0:
    cadastro['ano/contratação']=int(input('Qual o ano da sua contratação: '))
    cadastro['sálario']=float(input('Qual o seu sálario: '))
    cadastro['aposentadoria']=35-(datetime.now().year - cadastro['ano/contratação']) + cadastro['idade']

print(f'''
Nome: {cadastro['nome']}
Idade: {cadastro['idade']}''')
if cadastro['cdt']!=0:
    print(f'''
Carteira de Trabalho: {cadastro['cdt']}
 Ano de contratação: {cadastro['ano/contratação']}
 Sálario: {cadastro['sálario']}
 Aposentadoria: {cadastro["aposentadoria"]} anos''')
else:print('Carteira de trabalho: Não possui registro')  