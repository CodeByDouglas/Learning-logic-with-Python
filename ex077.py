palavras=('andar','correr','nadar','voar','saltar','escoregar')
vogais=('a','e','i','o','u')
for i in palavras:
    print(f'\nNa palvar {i} temos as seguintes vogais:',end='')
    for c in i:
        if c in vogais:
            print(c,'',end='')
