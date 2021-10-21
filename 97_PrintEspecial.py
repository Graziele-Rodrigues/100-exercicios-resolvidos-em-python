#definindo função
def titulo(texto):
    print('~'*len(texto)*2)
    print(texto.center(len(texto)*2,' '))
    print('~'*len(texto)*2)

#principal
msg = str.title(input('Informe uma mensagem: '))
titulo(msg)