# Escreva um programa que converta uma temperatura digitada em C e converta para F e K #
c =  float(input('Informa a temperatura em °C: '))
f = 9 * c /5 + 32
k = c + 273
print('A temperatura de {}°C corresponde a {:.1f}°F e {:.1f}°K'.format(c,f,k))