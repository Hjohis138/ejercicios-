
diccionario={'c1':'valor1','c2':'valor2'}  #estructura del diccionario clavey luego le asignao valor
print(type(diccionario)) #permite ver el tipo 
print(diccionario)

print(diccionario['c1']) #como se obitene valor de los diccionarios
resultado=diccionario['c1']
print(resultado)


paciente={'nombre':'Manuel',
         'apellido':'Pretti',
        'peso':82.6,
       'talla':1.76}
          
consulta=paciente['apellido']
print(consulta)
print(paciente['nombre'])
#print(paciente['peso'])
#print(paciente['talla'])

dic={'c1':55,'c2':[10,20,30],'c3':{'s1':100,'s2':200}}
#dicicionario tiene claves valores, lista y diccionario dentro de diccionarsioa
#'c2' es una lista
#'c3' diccionario
#'c1' clave
print(dic['c2'][1]) #estraer de la lista
print(dic['c3']['s2'])#estraer de un dicionario den tro de otro


dic_2={'c1':['a','b','c'],'c2':['d','e','f']}
print(dic_2['c2'][1].upper()) #obtener el string y colocarlo en mayuscula

#como agregar elementos a un diccionario
dic3={1:'a',2:'b'}
#agregar otro item clave y valor

print(dic3)
#modificar valores en un diccionarios mediante sus claves
dic3[2]='B' 
print(dic3)


#como puedo obtener todas las claves de un diccionarios
print(dic_2.keys())
#como puedo obtenr todos los valores
print(dic_2.values())

#como conocer claves y valores
print(dic_2.items())  #se indican tublas clave y su valor

#escribir 2 valores  crear dos variables e implier las mismas
dic4={'nombre':'johana','apellido':'herrera','edad':43,'peso':70}
var_1=dic4['nombre']
var_2=dic4['apellido']
var_3=dic4['edad']
var_4=dic4['peso']