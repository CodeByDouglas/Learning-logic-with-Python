valores=[]
for i in range(5):
    n=int(input('Incira um valor para lista:\n'))
    
    if i==0 or n>max(valores): 
        valores.append(n) 
        print('Item adicionado ao final da lista')
    else:
     for c in valores: 
        if n<=c:
            valores.insert(valores.index(c),n)
            print(f'Item adicionado a posição {valores.index(c)} da lista')
            break 
print(f'Valores digitados em ordem :{valores}')