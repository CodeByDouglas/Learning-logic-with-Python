def verific_vorto(nascimento):
    from datetime import datetime

    idade=datetime.now().year - nascimento
    if idade>18 and idade<65:
        return f'Com {idade} anos voto obrigatório'
    elif idade>=65:
        return f'Com {idade} anos voto opcional'
    else:
        return f'Com {idade} anos proibido votar'
    

anodenasc=int(input('Qual o ano em que você nasceu? '))
print(verific_vorto(anodenasc))
    
