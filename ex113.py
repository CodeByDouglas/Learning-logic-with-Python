from sys import exit

def valid_int():
    validade=False
    while not validade:
        try:
            validade=True
            nint=int(input('Insira um número inteiro: '))
        
        except KeyboardInterrupt:
            print('ERRO: O user decidiu encerrar o programa sem inserir uma valor')
            exit()
        except Exception:
            print('ERRO: por favor digite um número inteiro válido.')
            validade=False
    return nint



def valid_float():
    validade=False
    while not validade:
        try:
            validade=True 
            nfloat=float(input('Insira um número Real: '))
        except KeyboardInterrupt:
            print('ERRO: o user decidiu encerrar o progama sem inserir um número real.')
            exit()
        except Exception:
            print('ERRO: por favor digite um número real válido.')
            validade=False
        
    return nfloat



































# def inputint(frase):
#     print(frase)
#     while True:
#         uservar=input()
#         validador=0
        
#         for n in uservar:
#             if n in'0123456789':
#                 validador+=1     
        
#         if validador==len(uservar):
#             intvar=int(uservar)
#             break
#         else:
#             print('ERRO! Digite um número válido.')
#     return intvar    
        


# numero=inputint('Digite uma número inteiro:')
# print(f'Número tem o valor de {numero}')
