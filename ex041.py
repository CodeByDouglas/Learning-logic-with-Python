an=int(input('Qual o seu ano de nacimento?\n'))
idade=2024-an
if idade<=9:
    print('\nVocê é um nadador mirin!\n')
elif idade>9 and idade<=14:
    print('\nVocê é um nadador infantil!\n')
elif idade>14 and idade<=19:
    print('\nVocê é um nadador júnior!\n')
elif idade>19 and idade<=20:
    print('\nVocê é um nadador sênior!\n')
else:
    print('\nVocê é um nadador Master!')