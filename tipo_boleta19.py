#INPUT
cliente=input("Ingrese el nombre del cliente:")
famacia=input("Ingrese el nombre de la farmacia:")
pastillas=int(input("Ingrese Nr de pastillas:"))
pu=float(input("Ingrese precio unitario por pastilla:"))

# PROCESSING
total = (pu* pastillas)

#VERIFICADOR
compra=(total>19)

# OUTPUT
print("#######################")
print("# BOLETA DE VENTA")
print("#######################")
print("#")
print("# Cliente:  ", cliente)
print("# Farmacia:  ", famacia)
print("# Item   :  ",pastillas,"  Nr de pastillas")
print("# P.U.   :  S/.", pu)
print("# Total  :  S/.", total)
print("#######################")
