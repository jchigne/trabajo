#IMPUT
cliente=input("Nombres y Apellidos:")
nombre_tinda=input("Nonbre de la tienda=")
kg_naranjas=float(input("Precio unitario de las naranjas="))
cantidad=int(input("cantidad de naranjas="))

#PROCESSING
total= (kg_naranjas*cantidad)

#VERIFICADOR
compra=(total>10)

#OUTPUT
print("#######################################")
print("#  BOLETA DE VENTA 01")
print("#######################################")
print("#")
print("#cliente:  ",    cliente)
print("# Item   :  ",cantidad,"  Nr de naranjas")
print("P.U     : s/.",   kg_naranjas)
print("# TOTAL : s/.",      total)
print("#######################################")
