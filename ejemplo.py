
#1 ingresar texto

texto = input("Ingrese un texto de su preferencia: ")
letras=[]
texto.lower()
letras.append(input("Ingrese la primera letra de su elección: ".lower()))
letras.append(input("Ingrese la segunda letra de su elección: ".lower()))
letras.append(input("Ingrese la tercera letra de su elección: ".lower()) )

print("\n") #defino salto de línea

cantidad_letras1=texto.count(letras[0])
cantidad_letras2=texto.count(letras[1])
cantidad_letras3=texto.count(letras[2])

print(f"Hemos encontrado la letra {letras[0]} 
repetida {cantidad_letras1} veces")

print(f"Hemos encontrado la letra {letras[1]} 
repetida {cantidad_letras2} veces")

print(f"Hemos encontrado la letra {letras[2]} 
repetida {cantidad_letras3} veces")

print("\n") #defino salto de línea
print("CANTIDAD DE PALABRAS")
palabras=texto.split()
print(" HEMOS ENCONTRADO {len(palabras)} palabras en el texto")

print("\n") #defino salto de línea
print("letras de incio y fin")
letra_inicio=texto[0]
letra_fin=texto[-1]
print("la letra incial es {letra_inicio} y la latra final es {letra_fin}")

print("\n") #defino salto de línea
print("texto invertido")
palabras.reverse()
texto_invertido="".join(palabras)
print(f"Si ordenamos tu texto al revez va a decir {texto_invertido}")

print("\n") #defino salto de línea
print("buscando la palabra python")
buscar_python='pyton' in texto 
dic={True:'si', False:'no'}
print(f"la palabra python{dic[buscar_python]} se encuentra en el texto")
