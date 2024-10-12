def inputnumeric(frase):
    while True:
        num=str(input(f'{frase}')).strip()
        result=''
        negado=False
        flt=False
        numerico=False
        for x in num:
            if x.isnumeric()==True or x in ',.':
                if x in',.':
                    result+='.'
                    flt=True
                else:
                    result+=x
                    numerico=True
            else:
                negado=True
            
                
        if negado==True or numerico==False or result[len(result)-1]=='.' or result[0]=='.':
            print(f'ERRO:"{num}" é um preço inválido!')
        else: break
    
    if flt==True:
         return float(result)
    else:
        return int(result)

