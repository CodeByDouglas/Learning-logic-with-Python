Mapeso=0
Mepeso=0
for c in range(0,4):
    peso=float(input('Qual o seu peso?\n'))
    if peso>Mapeso:
        Mapeso=peso
        if Mepeso==0:
            Mepeso=peso
    elif peso<Mepeso:
        Mepeso=peso
print('O maior peso foi de {}\nO menor peso foi de {}'.format(Mapeso,Mepeso))