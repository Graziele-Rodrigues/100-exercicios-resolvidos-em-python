# Leia a data de nascimento de um atleta e classifique em mirim,infantil,junior,senior e master #
nascimento = int(input('Digite o ano do seu nascimento: '))
idade = 2020 - nascimento
if idade <=0:
    print('A ano de nascimento deve ser maior que o ano atual')
elif idade <=9: 
    print("Sua classificação é MIRIM")
elif idade>9 and idade <=14:
    print('Sua classificação é INFANTIL')
elif idade>14 and idade<=19:
    print('Sua classificação é JUNIOR')
elif idade>19 and idade<=25:
    print('Sua classificação é SÊNIOR')
else:
    print('Sua classificação é MASTER')