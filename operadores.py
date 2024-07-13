x=5
y=3

print(f"{x} mas {y} es igual a: {x+y}") #implementar operaciones utilizando cadenas
print(f"{x} menos {y} es igual a: {x-y}")
print(f"{x} por {y} es igual a: {x*y}")
print(f"{x} dividido {y} es igual a: {x/y}")
print(f"{x} dividido  {y} es igual a: {x//y}") #división al piso solo halla la parte entera del ejericicio de división
print(f"el residuo o modulo de {x} dividido {y} es igual a: {x%y}")
print(f" {x} elevado a la {y} es igual a: {x**y}")
print(f" {x} elevado a la {y} es igual a: {x**y}")
print(f"La raiz cuadras de {x} es igual a {x**0.5}")

#redondeo round
#l=x**0.5
#print(l)
#l=round(l,2)
#print(f"el redondeo del valor con dos cifras decimales de la raiz cuadrada de {x} es {l}")

#redondeo operación numerica
#print(90/7)
#print(round(90/7))

#redondeo con un numero de cifras decimales
#valor=95.6666687411
#valor=round(valor,3)
#print(f"el redondeo del valor con tres cifras decimales es {valor}")

# otra forma de redondear
raiz_cuadrada=x**0.5
numero_redondeado = round(raiz_cuadrada,2)
print(f"la raiz cuadrada de {x} es {numero_redondeado}")

valor=95.66665477
valor=round(valor)
print(type(valor))

