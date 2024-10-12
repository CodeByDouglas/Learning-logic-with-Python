from datetime import date
aa=date.today().year
maior=0
menor=0
for c in range(0, 7):
    an=(input('Qual o seu ano de nascimento?\n'))
    vr=type(an)
    if (vr==int)and(an>=1):
     if aa-an>21:
        maior += 1
     else:
        menor+= 1
    else:
       print('O ano iserido e inválido, insira um novo ano!')
print('O total de pesssoas maiores de idade é {}, e o total de pessoas menores de idade é {}'.format(maior,menor))