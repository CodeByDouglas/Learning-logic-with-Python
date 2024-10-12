ti=0
maiorI=0
Ifemininas=0

for c in range(0, 4):
 nome=(input('Qual o seu nome?\n'))
 idade=int(input('Qual a sua idade?\n'))
 sexo=str(input('Qual a seu sexo?\n')).strip().lower()
 ti+=idade
 if sexo=='masculino':
  if idade>maiorI:
   maiorI=idade
   Nhomen=nome
 if sexo=='feminino':
  if idade<20:
   Ifemininas+=1
med=ti/4
print('A média das idades é : {:.2f}\nO nome do homen mais velho é: {}\nA quantidade de mulheres com menos de 20 anos é:{}'.format(med,Nhomen,Ifemininas))
