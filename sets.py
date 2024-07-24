#no permite generar datos respetidos 
#no hay ordenamientos
#tres formas de estructurar conjuntos
mi_set=set([1,2,3,4]) #lista
mi_set1=set({1,2,3,4}) 
mi_set2=set((1,2,3,4))

print(mi_set)
print(mi_set1)
print(mi_set2)

print(type(mi_set))

#errores
#print(mi_set[0]) #no se puede extraer con posicionamiento por eso sale error
#mi_set[0]=5 #sale error no se puede modificar 

mi_set1={1,2,3,4,5,1,1,1,1}
print(mi_set1)
#inclui varios elementos 1 no los toma son como si no existieran
#no admite elementos duplicados

#longitud del conjunto
print(len(mi_set2))
#verificar si existe en el conjunto
print(2 in mi_set2)


#unir conjuntos c/u tine el 3 pero solo aparece union
s1={1,2,3}
s2={3,4,5}
s3=s1.union(s2)
print(s3)

#agregar elementos al conjunto add
s1.add(4)
print(s1)

#eliminar un elemento remove
s1.remove(3)
print(s1)

#eliminar un elemento no existe sale error remove
s1.remove(5)
print(s1)


#eliminar un elemento no existe sale error discard
s1.discard(5)
print(s1)

#no sale eroor pero si elimina

s1.clear() #remuevo toso los elementos conjuto vacio
print(s1)