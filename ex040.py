not1=float(input('Qual a sua nota do primeiro bimestre ?\n'))
not2=float(input('\nQual a sua nota do segundo bimestre ?\n'))
not3=float(input('\nQual a sua nota do terceiro bimestre?\n'))
med=float((not1+not2+not3)/3)
#print('Sua média foi de {} '.format(med))
if (not1>=0 and not1<=10)and((not2>=0)and(not2<=10))and((not3>=0)and(not3<=10)):
 if med>=0 and med<5:
    print('Aluno reprovado!\nMédia = {:.1f}'.format(med))
 elif med>=5 and med<=6.9:
    print('Aluno de recuperação!\nMédia = {:.1f}'.format(med))
 elif med>=7 and med<=10:
    print('Aluno aprovado!\nMédia = {:.1f}'.format(med))
else:
 print('Algo deu errado, possivelmente alguma nota fora do padrão esperado.\nPORFAVOR REINSIRA AS NOTAS!!')