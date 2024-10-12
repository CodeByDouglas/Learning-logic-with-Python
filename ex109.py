import utilidadesCeV.moeda as moeda

preço=float(input('Insira o preço: '))
print(f'''
A metade de R${preço} é {moeda.metade(preço,False)}
O dobro de R${preço} é {moeda.dobro(preço,True)}
Aumentando 10%, temos {moeda.aumento(preço, 10, True)}
Reduzindo 13%, temos {moeda.reduçao(preço, 13, True)}
''')