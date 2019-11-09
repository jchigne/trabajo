#INPUT
cliente=input("Ingrese el nombre del cliente:")
mesero=input("Ingrese el nombre del mesero:")
chicharon=int(input("Ingrese Nr de chicharones:"))
pu_chicharon=float(input("Ingrese precio unitario:"))

# PROCESSING
total = (pu_chicharon* chicharon)

#VERIFICADOR
compra=(total>18)

# OUTPUT
print("#######################")
print("# BOLETA DE VENTA")
print("#######################")
print("#")
print("# Cliente:  ", cliente)
print("# Mesero:  ", mesero)
print("# Item   :  ",chicharon,"  Nn de chicharones")
print("# P.U.   :  S/.", pu_chicharon)
print("# Total  :  S/.", total)
print("#######################")
