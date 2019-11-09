#INPUT
cliente=input("Ingrese el nombre del cliente:")
mesero=input("Ingrese el nombre del mesero:")
aji_gallinas=int(input("Ingrese Nr de aji de gallinas:"))
pu_aji=float(input("Ingrese precio unitario:"))

# PROCESSING
total = (pu_aji*aji_gallinas)

#VERIFICADOR
compra=(total>11)

# OUTPUT
print("#######################")
print("# BOLETA DE VENTA")
print("#######################")
print("#")
print("# Cliente:  ", cliente)
print("# Mesero:  ", mesero)
print("# Item   :  ",aji_gallinas,"  Nr de ajis")
print("# P.U.   :  S/.", pu_aji)
print("# Total  :  S/.", total)
print("#######################")
