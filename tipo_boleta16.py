#INPUT
cliente=input("Ingrese el nombre del cliente:")
ferreteria=input("Ingrese el nombre de la ferreteria:")
ladrillos=int(input("Ingrese Nr de ladrillos:"))
millar=float(input("Ingrese precio por millar:"))

# PROCESSING
total = (ladrillos*millar)

#VERIFICADOR
compra=(total>100)

# OUTPUT
print("#######################")
print("# BOLETA DE VENTA")
print("#######################")
print("#")
print("# Cliente:  ", cliente)
print("# Ferretaria:  ", ferreteria)
print("# Item   :  ",ladrillos," millares de ladrillos")
print("# P.U.   :  S/.", millar)
print("# Total  :  S/.", total)
print("#######################")
