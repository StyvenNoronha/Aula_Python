Nome = input('Digite seu nome')
Altura = float(input('Digite sua altura'))
Peso = int(input('Digite seu peso '))
imc = Peso / (Altura * Altura)


print(f'{Nome} tem {Altura:.2f} de altura')
print(f'pesa {Peso} quilos e seu IMC é {imc:.2f}')
