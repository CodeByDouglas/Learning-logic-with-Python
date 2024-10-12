import requests

def verifc_sit(url):
    acesso=True
    try:
        verificando=requests.get(url)
    except requests.exceptions.RequestException:
        acesso=False
    if acesso:
        print(verificando.read())
        return 'Site acessado com sucesso!'
    else:
        return 'Erro ao acessar o site'


site=str(input('Insira a URL do site: '))
print(verifc_sit(site))
