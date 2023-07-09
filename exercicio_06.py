user = input('Digite seu CPF: ')

CPF = user.replace('.', '').replace('-', '')    #remove os pontos e traços
print(CPF)

#primeiro digito
noveDigitos = CPF[0:9]
contadorR = 10
resul = 0
for i in noveDigitos:
    resul += int(i) * contadorR
    contadorR -= 1
digito = ((resul*10)%11)




#segundo digito
print('Seu primeiro digito é: ', digito if digito<=9 else 0)
dezDigitos = noveDigitos + str(digito)
contador = 11
resul = 0
for i in dezDigitos:
    resul += int(i) * contador
    contador -= 1   
digito1 = ((resul*10)%11)
print('Seu segundo digito é: ', digito1 if digito1<=9 else 0)

print(f'seus digitos são: {digito}{digito1}')
vCPF = int(CPF[9:10])
vCPF1 = int(CPF[10:11])
print(vCPF)
print(vCPF1)

if vCPF == digito and vCPF1 == digito1:
    print('CPF Válido')
else:    
    print('CPF Inválido')

