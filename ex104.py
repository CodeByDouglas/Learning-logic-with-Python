def inputint(frase):
    print(frase)
    while True:
        uservar=input()
        validador=0
        
        for n in uservar:
            if n in'0123456789':
                validador+=1     
        
        if validador==len(uservar):
            intvar=int(uservar)
            break
        else:
            print('ERRO! Digite um número válido.')
    return intvar    
        


numero=inputint('Digite uma número inteiro:')
print(f'Número tem o valor de {numero}')