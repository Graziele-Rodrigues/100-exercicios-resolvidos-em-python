import math
angulo = float(input('Digite o ângulo que você deseja: '))
sen = math.sin(math.radians(angulo))
cos = math.cos(math.radians(angulo))
tan = math.tan(math.radians(angulo))
print('O ângulo de {:.1f} tem o SENO de {:.1f}'.format(angulo, sen))
print('O ângulo de {:.1f} tem o COSSENO de {:.1f}'.format(angulo, cos))
print('O ângulo de {:.1f} tem a TANGENTE de {:.1f}'.format(angulo, tan))