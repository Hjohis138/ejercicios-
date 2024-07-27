# listas se entiende con []

nombre=['Juan', 'Luis', 'Melisa']
#imprime la lista
print(nombre)
#imprime el elemento
print(nombre[1])
#si deseo imprimir el ultimo elemento [-1]
print(nombre[-1])
#como implementar iterar para sacer la información  solo quiero que saque a cada uno y lo imprima
#que avance de uno a uno
#ciclo se hace con un for


#se puede colocar un rango de impresión 
#el solo toma el punto de partida y no el de finalización 
print(nombre[0:2])
print(nombre[:2])
print(nombre[1:])
#nodificación de elementos
nombre[1]='Maria'
print(nombre)
#longitud de la lista leng
print(len(nombre))
#append agrega literal de información al final
nombre.append('Johan')
print(nombre)

#insertar en una posición específico
nombre.insert(1,'laura')

print(nombre)
nombre.remove('Maria')
print(nombre)

#quita el untimo elemento
nombre.pop()
print(nombre)

#eliminar la posición
del nombre[0]
print(nombre)

#limpiar la lista
nombre.clear()
print(nombre)

#eliminar lista
#del nombre
#print(nombre)

#Tuplas
#no se puede añadir dismuniro o cambiar valores
#como identificar lista[] tuplas ()

milista=["Rojo","Azul","Verte"]
print(type(milista))
miTupla=("Rojo","Azul","Verte")
print(type(miTupla))

milista[0]="Amarillo"
print(milista[0])

#miTupla[0]="azul"
#print(miTupla[0])
#el erro dice que esto no soporta este tipó de cambio

#conjuntos de datos set se define con {}
miconjunto={1,2,3,4,5,6,7,8,9}
print(miconjunto)
print(type(miconjunto))

#los conjunto permite remover agregar

#añadir datos
miconjunto.add(10)
print(miconjunto)

miconjunto.add(8)
print(miconjunto)

miconjunto.remove(10)
print(miconjunto)

miconjunto.remove(8)
print(miconjunto)

#debugin es un herramiento de desarrollo  yuno quiere hacer el ejercicio de como se hace lentamente el ejercicio
#breakpoint se ubca con el punto rojo o abrir  y clkic y añadir un debugin
#despacio el elemento  para antes de continuar

#diccionario dato más interesante dentro de el se almacena todo
#se puede almacenr una tupla dentro de la lista pero se puierde orden 
#crear un diccionario es como la variable mayor de pyton
#definen el valor mediante el nombre y valor
midiccionario={"nombre1":"juan david" , "edad":25, "carrera": "ingeniero"}
print(midiccionario)

#crear diccionario dentro de otro 
midicionario1={
    "1":{"nombre1":"juan david" , "edad":25, "carrera": "ingeniero"},
    "2":{"nombre1":"marcos" , "edad":45, "carrera": "quimico"},
    "3":{"nombre1":"felipe" , "edad":20, "carrera": "docente"}
}
#print(midicionario1)

print(midicionario1[3])

               


