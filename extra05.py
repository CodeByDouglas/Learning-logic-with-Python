iguais=0
palavra1=str(input())
palavra2=str(input())

for c in palavra1:
 if c in palavra2:
  iguais+=1

if iguais==len(palavra2):
 print('anagramas')
else:
 print('não são')
