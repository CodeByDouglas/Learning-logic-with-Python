abertura=fechamento=0
expressoes=[str(input('Insira a sua expressão')).upper().strip()]

for c in expressoes[0]:
    if c=='(':
        abertura+=1
    elif c==')':
        fechamento+=1
if abertura==fechamento: print('Expressão valida')
else: print('Expressão invalida')   