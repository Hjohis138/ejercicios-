lista_1=['a','b','c','d']
lista_2=['1','2','3','4']
lista_3=["hola",2,5.3,['a','b']]

print(type(lista_1)) #definir que tipo de lementos es 

resultado=lista_1[2] #acceder al elemento 2
print(resultado)

resultado=lista_1[0:2] #solo hasta el elmentos 2
print(resultado)

resultado=lista_1[:] #solo de inidio a final
print(resultado)


print(lista_1 + lista_2+lista_3) #junta lista

#las litas son mutables

lista_2[0]='bienvenido' #asigne un nuevo valor
print(lista_2)

print(lista_1)
lista_1.append('g') #agregar un elemento al ultimo de la lista
print(lista_1)

print(lista_2)
lista_2.pop() #elimina el ultimo elemento de la lista
print(lista_2)

lista_2.pop(0) #elimina el  elemento de la lista que yo le indique
print(lista_2)

print(lista_3)
