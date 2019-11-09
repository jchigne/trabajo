#INPUT
cliente=input("Ingrese el nombre del cliente:")
mesero=input("Ingrese el nombre del mesero:")
cebiches=int(input("Ingrese Nr de cebiches:"))
pu_cebiche=float(input("Ingrese precio unitario:"))

# PROCESSING
total = (pu_cebiche* cebiches)

#VERIFICADOR
compra=(total>11)

# OUTPUT
print("#######################")
print("# BOLETA DE VENTA")
print("#######################")
print("#")
print("# Cliente:  ", cliente)
print("# Mesero:  ", mesero)
print("# Item   :  ",cebiches,"  Nr de cebiches")
print("# P.U.   :  S/.", pu_cebiche)
print("# Total  :  S/.", total)
print("#######################")
