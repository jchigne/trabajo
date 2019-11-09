#INPUT
cliente=input("Ingrese el nombre del cliente:")
bodega=input("Ingrese el nombre de la bodega:")
azucar=int(input("Ingrese  kg de azucar:"))
pu=float(input("Ingrese precio unitario del kg de azucar:"))

# PROCESSING
total = (pu* azucar)

#VERIFICADOR
compra=(total>15)

# OUTPUT
print("#######################")
print("# BOLETA DE VENTA")
print("#######################")
print("#")
print("# Cliente:  ", cliente)
print("# Bodega:  ", bodega)
print("# Item   :  ",azucar,"  kg de azucar")
print("# P.U.   :  S/.", pu)
print("# Total  :  S/.", total)
print("#######################")
