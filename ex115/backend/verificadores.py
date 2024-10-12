def valid_int(frase):
    validade=False
    while not validade:
        try:
            validade=True
            nint=int(input(f'{frase}'))
        
        except Exception:
            print('ERRO: por favor digite um número inteiro válido.')
            validade=False
    return nint


def valid_str(frase):
    validade=False
    while not validade:
        try:
            validade=True
            nint=str(input(f'{frase}'))
        
        except Exception:
            print('ERRO: por favor digite um nome válido.')
            validade=False
    return nint


def valid_opção(frase):
    while True:
        nint=valid_int(frase)
        if nint<1 or nint>3:
            print('Erro: incira um número válido.')
        else:
            break 
    return nint