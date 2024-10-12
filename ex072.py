Nextenso=('zero','um','dois','tres','quatro','cinco','seis',
          'sete','oito','nove','dez','onze','doze','treze',
          'quatorze','quinze','dezeseis','dezesete','dezoito',
          'dezenove','vinte')
while True:
    numero=int(input('Digite um número entre 0 e 20:'))
    while numero>20 or numero<0:
        numero=int(input('Número inválido, digite um número entre 0 e 20:'))

    print(f'Você digitou o número {Nextenso[numero]}')
    validaçao=str(input('Deseja continuar?\n[S]-sim [N]-não\n')).upper().strip()[0]
    if validaçao=='N': break