nm=int(input('Insira um número para converter para outra basa:\n'))
base=int(input('1 - BINARIO\n2 - OCTAL\n3 - HEXADECIMAL\n'))
if base==1:
    print('{}'.format(bin(nm)[2:]))
elif base==2:
    print('{}'.format(oct(nm)[2:]))
elif base==3:
    print('{}'.format(hex(nm)[2:]))