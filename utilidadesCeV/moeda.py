def metade(valor,format=False):
    if format==True: 
        return formataçao( valor/2)
    else:
        return valor/2


def dobro(valor,format=False):
    if format==True: 
        return formataçao( valor*2)
    else:
        return valor*2


def aumento(valor, porcentagem,format=False):
    if format==True: 
        return formataçao( ((valor*porcentagem)/100)+valor)
    else:
        return ((valor*porcentagem)/100)+valor


def reduçao(valor, porcentagem,format=False):
    if format==True: 
        return formataçao( valor-((valor*porcentagem)/100))
    else:
        return valor-((valor*porcentagem)/100)


def formataçao(valor):
    
    return f'R${valor:>.2f}'.replace('.', ',') 
    

def resumo(p, a, r):
    print(f'''
{30*'-'}
{('RESUMO DO VALOR').center(30)}
{30*'-'}
Preço analizado: {formataçao(p)}
Dobro do preço:\t{dobro(p,True)}
Metade do prço:\t{metade(p,True)}
{a}% de aumento:\t{aumento(p, a, True)}
{r}% de redução:\t{reduçao(p, r, True)}
{30*'-'}''')