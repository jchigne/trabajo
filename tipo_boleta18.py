#INPUT
cliente=input("Ingrese el nombre del cliente:")
libreria=input("Ingrese el nombre de la libreria:")
obras=int(input("Ingrese Nr de obras:"))
pu=float(input("Ingrese precio unitario por obras:"))

# PROCESSING
total = (pu* obras)

#VERIFICADOR
compra=(total>18)

# OUTPUT
print("#######################")
print("# BOLETA DE VENTA")
print("#######################")
print("#")
print("# Cliente:  ", cliente)
print("# Libreria:  ", libreria)
print("# Item   :  ",obras,"  Nr de obras")
print("# P.U.   :  S/.", pu)
print("# Total  :  S/.", total)
print("#######################")
