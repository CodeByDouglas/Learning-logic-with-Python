from datetime import date

dn=int(input('Em qual ano vc naceu ?\n '))
ano=date.today().year
idade= ano-dn
if idade>18:
    print('Você passou {} anos  da idade de se alistar'.format(idade-18))
elif idade==18:
    print('Você esta na idade de se apresentar ao exercíto')
else:
    print('faltam {} anos para vc se apresentar ao exercíto'.format(18-idade))