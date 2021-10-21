# leia 3 segmentos e diga se é possivel formar triangulo e caso seja possível diga o tipo #
r1 = float(input('Primeiro segmento: '))
r2 = float(input('Segundo segmento: '))
r3 = float(input('Terceiro segmento: '))
if r1<r2+r3 and r2 <r1+r3 and r3<r1+r2:
    if r1==r2 and r2==r3:
        print('Os segmentos acima PODEM formar um triângulo EQUILÁTERO')
    elif r1 != r2 and r2 != r3 and r1!=r3:
        print('Os segmentos acima PODEM formar um triângulo ESCALENO')
    else:
        print('Os segmentos acima PODEM formar um triângulo ISÓCELES')
else:
    print('Os segmentos acima NÃO PODEM formar um triângulo') 