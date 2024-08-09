
#1 ingresar texto

texto = input("Ingrese un texto de su preferencia: ")
letras=[]
texto.lower()
letras.append(input("Ingrese la primera letra de su elección: ".lower()))
letras.append(input("Ingrese la segunda letra de su elección: ".lower()))
letras.append(input("Ingrese la tercera letra de su elección: ".lower()) )

print("\n") #defino salto de línea

print("CANTIDAD DE LETRAS")
palabras=texto.split()
print(Hemos encontrado {len(palabras)} palabras en tu texto)
cantidad_letras1=texto.count(letras[0])
cantidad_letras2=texto.count(letras[1])
cantidad_letras3=texto.count(letras[2])

print(f"Hemos encontrado la letra {letras[0]} 
repetida {cantidad_letras1} veces")

print(f"Hemos encontrado la letra {letras[1]} 
repetida {cantidad_letras2} veces")

print(f"Hemos encontrado la letra {letras[2]} 
repetida {cantidad_letras3} veces")

#2 almacenar el texto en una lista


def contar_letras(texto, letras):
  """
  Cuenta la cantidad de apariciones de cada letra en el texto.

  Args:
    texto: El texto a analizar.
    letras: Una lista de letras a buscar.

  Returns:
    Un diccionario que contiene la cantidad de apariciones de cada letra.
  """
  conteo_letras = {}
  for letra in letras:
    conteo_letras[letra] = 0
  for letra in texto.lower():
    if letra in letras:
      conteo_letras[letra] += 1
  return conteo_letras

def contar_palabras(texto):
  """
  Cuenta la cantidad de palabras en el texto.

  Args:
    texto: El texto a analizar.

  Returns:
    La cantidad de palabras en el texto.
  """
  palabras = texto.split()
  return len(palabras)

def obtener_primera_letra(texto):
  """
  Obtiene la primera letra del texto.

  Args:
    texto: El texto a analizar.

  Returns:
    La primera letra del texto.
  """
  return texto[0]

def obtener_ultima_letra(texto):
  """
  Obtiene la última letra del texto.

  Args:
    texto: El texto a analizar.

  Returns:
    La última letra del texto.
  """
  return texto[-1]

def obtener_longitud_texto(texto):
  """
  Obtiene la longitud del texto.

  Args:
    texto: El texto a analizar.

  Returns:
    La longitud del texto.
  """
  return len(texto)

conteo_letras = contar_letras(texto, letras)
print("Cantidad de apariciones de cada letra:")
for letra, cantidad in conteo_letras.items():
  print(f"{letra}: {cantidad}")

cantidad_palabras = contar_palabras(texto)
print(f"Cantidad de palabras: {cantidad_palabras}")

primera_letra = obtener_primera_letra(texto)
print(f"Primera letra: {primera_letra}")

ultima_letra = obtener_ultima_letra(texto)
print(f"Última letra: {ultima_letra}")

longitud_texto = obtener_longitud_texto(texto)
print(f"Longitud del texto: {longitud_texto}")