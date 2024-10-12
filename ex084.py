salvarpessoas=[]
receberpessoas=[]
maiorp=[]
menorp=[]
while True:
    receberpessoas.append(str(input('Nome: ')))
    receberpessoas.append(str(input('Peso: ')))
    salvarpessoas.append(receberpessoas[:])
    receberpessoas.clear()
    verific=str(input('Deseja continuar?   [S/N]\n')).upper().strip()
    if verific=='N':
        break
for p in salvarpessoas:
    if salvarpessoas.index(p)==0:
        maiorp.append(p[1])
        maiorp.append(p[0])
        
        menorp.append(p[1])
        menorp.append(p[0])
    else:
        if p[1]>maiorp[0]:
            maiorp.clear()
            maiorp.append(p[1])
            maiorp.append(p[0])
        elif p[1]==maiorp[0]:
            maiorp.append(p[0])
        if p[1]<menorp[0]:
            menorp.clear()
            menorp.append(p[1])
            menorp.append(p[0])
        elif p[1]==menorp[0]:
            menorp.append(p[0])
print(f'''
Foram inseridas {len(salvarpessoas)} no total.
O maior peso foi de {maiorp[0]}, peso de {maiorp[1:]}.
O menor peso foi de {menorp[0]}, peso de {menorp[1:]}.
''')
 
           




