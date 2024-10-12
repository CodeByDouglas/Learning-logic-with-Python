from random import randint
from time import sleep

print('Olá, vamos jogar jokenpô?\n 1-start 2-Sair\n')
inc=int(input())
if inc==1:
    print('\nVamos lá, digite\n1-Para pedra\n2-Para papel\n3-Para tesoura')
    
    j=int(input())
    m =int(randint(1,3))
    print('JO...')
    sleep(1)
    print('KEN...')
    sleep(1)
    print('PÔ!!!\n')
    sleep(0.5)
    if (j==1)and(m==1):
        print('Jogador || Maquina\nPEDRA vs PEDRA\n    EMPATE!')
    elif (j==2)and(m==2):
        print('Jogador || Maquina\nPAPEL vs PAPEL\n    EMPATE!')
    elif (j==3)and(m==3):
        print('Jogador || Maquina\nTESOURA vs TESOURA\n    EMPATE!')
    elif (j==1)and(m==2):
        print('Jogador || Maquina\nPEDRA vs PAPEL\n    MAQUINA WIN!')
    elif (j==2)and(m==1):
        print('Jogador || Maquina\nPAPEL vs PEDRA\n    JOGADOR WIN!')
    elif (j==3)and(m==1):
        print('Jogador || Maquina\nTESOURA vs PEDRA\n    MAQUINA WIN!')
    elif (j==1)and(m==3):
        print('Jogador || Maquina\nPEDRA vs TESOURA\n    JOGADOR WIN!')
    elif (j==2)and(m==3):
        print('Jogador || Maquina\nPAPEL vs TESOURA\n    MAQUINA WIN!')
    elif (j==3)and(m==2):
        print('Jogador || Maquina\nTESOURA vs PAPEL\n    JOGADOR WIN!')
    else:
        print('jogada invalída!')

else:
    print('OK, Obrigado!')