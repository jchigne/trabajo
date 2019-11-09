#INPUT
cliente=input("Ingrese el nombre del cliente:")
sacos_arroz=int(input("Ingrese Nr de sacos de arroz:"))
pu_arroz=float(input("Ingrese precio unitario:"))

# PROCESSING
total = (pu_arroz* sacos_arroz)

#VERIFICADOR
compra=(total>11)

# OUTPUT
print("#######################")
print("# BOLETA DE VENTA")
print("#######################")
print("#")
print("# Cliente:  ", cliente)
print("# Item   :  ",sacos_arroz,"  Nr de sacos de arroz")
print("# P.U.   :  S/.", pu_arroz)
print("# Total  :  S/.", total)
print("#######################")
