listadeP=('Caderno',5.00,'Lápis',1.00,'Caneta',2.00,'Borracha',0.50,'Mochila',100.00,)
print('-'*30,'\nLISTA DE PREÇOS\n','-'*30)

for i in range(0,len(listadeP),2):
    print(f'{listadeP[i]:.<20}R${listadeP[i+1]}')
print('-'*30)