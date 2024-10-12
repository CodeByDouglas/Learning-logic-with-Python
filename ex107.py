import utilidadesCeV.moeda as moeda

preço=float(input('Insira o preço: '))
print(f'''
A metade de {preço} é {moeda.metade(preço)}
O dobro de {preço} é {moeda.dobro(preço)}
Aumentando 10%, temos {moeda.aumento(preço, 10)}
Reduzindo 13%, temos {moeda.reduçao(preço, 13)}
''')







