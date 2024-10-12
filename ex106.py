def helppy(comand):
    print(help(comand))
while True:
    dica=str(input('Insira uma comando ou biblioteca: '))
    helppy(dica)
    if dica=='N': break
