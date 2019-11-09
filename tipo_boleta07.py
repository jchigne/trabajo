#INPUT
cliente=input("Ingrese el nombre del cliente:")
mesero=input("Ingrese el nombre del mesero:")
leche_tigre=int(input("Ingrese Nr de leches de tigres:"))
pu_leche=float(input("Ingrese precio unitario:"))

# PROCESSING
total = (pu_leche* leche_tigre)

#VERIFICADOR
compra=(total>13)

# OUTPUT
print("#######################")
print("# BOLETA DE VENTA")
print("#######################")
print("#")
print("# Cliente:  ", cliente)
print("# Mesero:  ", mesero)
print("# Item   :  ",leche_tigre,"  Vasos de leche")
print("# P.U.   :  S/.", pu_leche)
print("# Total  :  S/.", total)
print("#######################")
