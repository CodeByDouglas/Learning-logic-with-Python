import utilidadesCeV.moeda as moeda 

preço=float(input('Insira o preço: '))
print(f'''
A metade de {preço} é {moeda.formataçao(moeda.metade(preço))}
O dobro de {preço} é {moeda.formataçao(moeda.dobro(preço))}
Aumentando 10%, temos {moeda.formataçao(moeda.aumento(preço, 10))}
''')