#definicion de una tupla
#entre perentesisi sus elementos
mi_tupla=(1,2,3,4)
print(mi_tupla)
print(type(mi_tupla))

#las tuplas pueden tener diferentes caracteristiaca
t1=(5,4.5,"hola")
print(t1)

#mi_tupla[0]=5 
#no se puede debido a que son inmutaple por eso sale error
#print(mi_tupla) 

mi_tupla2=(1,2,(10,20),4)
print(mi_tupla2)
#obtener un elemento en tuplas se accede con posicionamiento
print(mi_tupla2[2][0])
#las tuplas se pueden convertir en litas
mi_tupla=list(mi_tupla)
print(mi_tupla)  #aqui ya se muestra como una lista
print(type(mi_tupla))
#convertir lista en tupla se lllam casteto
mi_tupla=tuple(mi_tupla)
print(type(mi_tupla))
#creo una tupla
t2=(1,2,3)
#asigno valores a las varibles los valores de la tupla
x,y,z=t2
print(x,y,z)
#ojo funciona si tenemos mismo numero de variables y elementos 

#si se desea obtener la losgitud de la tupla
print(len(t2))

#contar el numero de apariciones de un elemento
t3=(1,2,3,1)
print(t3.count(1))

#tuplas guarda información que no se va a modificar 
#ejem configuraciones por ejemplo 




