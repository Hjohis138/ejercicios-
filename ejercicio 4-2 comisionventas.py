def calcular_comision(nombre, ventas):
  
  # Calcular la comisión (13% del total de ventas)
  comision = ventas * 0.13

  # mensaje con la información del vendedor y la comisión
  mensaje = f"""
  Vendedor: {nombre}
  Ventas totales: ${ventas:.2f}
  Comisión: ${comision:.2f}
  """

  return mensaje

# ingresar nombre del vendedor 
nombre_vendedor = input("Ingrese el nombre del vendedor: ")

# ingresar el monto de las ventas 
monto_ventas = float(input("Ingrese el monto de las ventas: $"))

# Calculando la comisión 
comision_mensaje = calcular_comision(nombre_vendedor, monto_ventas)
print(comision_mensaje)
