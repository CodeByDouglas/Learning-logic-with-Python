notas50=notas20=notas10=notas10=notas1=0
saque=int(input('Qual valor você deseja sacar:\n'))
while True:
    if saque>=50:
        saque-=50
        notas50+=1
    elif saque>=20:
        saque-=20
        notas20+=1
    elif saque>=10:
        saque-=10
        notas10+=1
    elif saque>=1:
        saque-=1
        notas1+=1
    else:
        break
print(f'Total de {notas50} notas de R$50\n'if notas50!=0 else'',end='')
print(f'Total de {notas20} notas de R$20\n'if notas20!=0 else'',end='')
print(f'Total de {notas10} notas de R$10\n'if notas10!=0 else'',end='')
print(f'Total de {notas1} notas de R$1\n'if notas1!=0 else'',end='')