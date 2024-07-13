
# ingresar nombre del vendedor 
nombre_vendedor = input("Ingrese el nombre del vendedor: ")

# ingresar el monto de las ventas 
monto_ventas = float(input("Ingrese el monto de las ventas: $"))

#calculo de comisión
comision = monto_ventas * 0.13
comision=round(comision,2)

#imprimir los valores
print(f" Vendedor: {nombre_vendedor} \n  Ventas totales: ${monto_ventas} \n comisión del vendedor {comision}")


