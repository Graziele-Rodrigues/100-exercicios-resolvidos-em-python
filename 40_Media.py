# de acordo com as notas diga se foi aprovado ou ano #
n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
n3 = float(input('Digite a terceira nota: '))
media = (n1+n2+n3)/3
if media >= 7:
    print('Sua nota foi {:.1f} - APROVADO'.format(media))
elif media>=5 and media < 7:
    print('Sua nota foi {:.1f} - RECUPERAÇÃO'.format(media))
else:
    print('Sua nota foi {:.1f} - REPROVADO'.format(media))
