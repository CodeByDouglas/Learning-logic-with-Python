def gera_etiqueta(txt):
    print(f'''
{len(txt)*'~'}
{txt}
{len(txt)*'~'}''')
    
texto=str(input('Insira a frase: '))
gera_etiqueta(texto)

