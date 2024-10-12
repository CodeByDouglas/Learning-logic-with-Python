import random
acertou=False
cont=1
print('Olá vamos brincar de advinhação, estou pensando em um número de 0 a 10, tente adivinhar qual é \n')
numeropc=random.randint(0,10)
while not acertou:
 numerojg=int(input('Qual o seu número ?\n'))
 if numerojg==numeropc:
    print('Parábens Você acretou em {} tentativas!!!'.format(cont))
    acertou=True
 else:
    print('Você errou tente novamente!\n')
    acertou=False
 cont+=1  