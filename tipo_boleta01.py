#IMPUT
cliente=input("Nombres y Apellidos:")
nombre_tinda=input("Nonbre de la tienda=")
gaseosas=float(input("Precio unitario de la gaseosas="))
cantidad=int(input("cantidad de gaseosas="))

#PROCESSING
total= (gaseosas*cantidad)

#VERIFICADOR
compra=(total>20)

#OUTPUT
print("#######################################")
print("#  BOLETA DE VENTA 01")
print("#######################################")
print("#")
print("#cliente:  ",    cliente)
print("# Item   :  ",cantidadg,"  Nr de gaseosas")
print("P.U     : s/.",   gaseosas)
print("# TOTAL : s/.",      total)
print("#######################################")
