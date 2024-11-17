print("="*60)
print("Bem vindo a Calculadora bem útil.")
print("="*60)
massa = float(input("Insira sua massa corporal:"))
alt = float(input('Insira sua altura:'))
print('='*60)

carbsbk = massa * 8
protbk = massa * 2
gordbk = massa * 1.5
carbsct = massa * 5
protct = massa * 2
gordct = massa * 1
imc = massa // alt**2
creatina = massa * 0.05
agua = massa * 35

pergunta1 = str(input('Você deseja fazer um cutting ou um bulking?'))
print('='*60)

if pergunta1 == 'bulking':
    print('Para montar uma dieta de bulking baseada no seu peso corporal você deve comer:')
    print('{}g de carboidrato'.format(carbsbk))
    print('{}g de proteína'.format(protbk))
    print('{}g de gordura'.format(gordbk))
    print('='*60)
else: 
    print('Para montar uma dieta de cutting baseada no seu peso corporal você deve comer:')
    print('{}g de carboidratos'.format(carbsct))
    print('{}g de proteína'.format(protct))
    print('{}g de gordura'.format(gordct))
    print('='*60)

print('Além disso, para ter um bom resultado na academia você deve consumir:')
print('{}g de creatina e {}ml de água'.format(creatina, agua))
print('='*60)

pergIMC = str(input('Você deseja calcular seu IMC?'))
print('='*60)

if pergIMC == 'sim':
    print('Seu IMC corresponde a {}'.format(imc))
    print('='*60)
    print('Obrigado por utilizar a calculadora bem útil.')
else: print('Obrigado por utilizar a calculadora bem útil.') 
 
print('='*60)