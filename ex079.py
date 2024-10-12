lista=[]
while True:
    n=int(input('Insira um valor na lista:'))
    if n not in lista: lista.append(n)
    verific=str(input('Deseja inserir outro valor a lista?\n[S]-sim [N]-não\n')).upper().strip()[0]
    if verific == 'N': break
print(f'Os números digitados foram : {lista}')
print(f'Lista em ordem : {sorted(lista)}')
