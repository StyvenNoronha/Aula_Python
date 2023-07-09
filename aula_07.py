'''
lista = ['styven',24,2.5]


print(lista[2])
del lista[2] #deletar algim item da lisya
print(lista)
lista.append(50) #adicionar item na lista
print(lista)
lista.pop(0)# remover o item selecionado
lista.append(41)
print(lista)
lista.append(22)
del lista[-1]# deletar o ultimo item da lista
lista.clear()
print(lista)

listaA = [ 1,2,3,4,5,6]
listaB = [7,8,9,10]

print(listaA)
print(listaB)

listaA.extend(listaB)

print(listaA)

listaA.insert(-1,5)
print(listaA)


listaA = [ 1,2,3,4,5,6]

for lis in listaA:
    print(lis)

'''

_,_,nomes, *_ = ['styven','joao','maria','pedro','jose']
nome = 'styven','joao','maria','pedro','jose' #tupla e imultavel nunca mudar

print(nomes)
print(nome)
