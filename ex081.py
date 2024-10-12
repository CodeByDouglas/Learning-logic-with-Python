numero=[]
while True:
 n=(int(input('Insira um número na lista:\n')))
 numero.append(n)
 verifc=str(input('Deseja comtinuar a inserir números?\n[S]|[N]\n')).upper().strip()[0]
 if verifc=='N': break
 
print(f'''
Foram digitados {len(numero)} valores.
Lista em ordem decrescente : {sorted(numero,reverse=True)} ''')
print('O valor cinco faz parte da lista!' if 5 in numero else 'O valor cinco não faz parte da lista')