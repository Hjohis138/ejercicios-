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

