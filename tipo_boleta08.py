#INPUT
cliente=input("Ingrese el nombre del cliente:")
mesero=input("Ingrese el nombre del mesero:")
Entrada=int(input("Ingrese Nr de entradas:"))
pu_entradas=float(input("Ingrese precio unitario:"))

# PROCESSING
total = (pu_entradas*Entrada)

#VERIFICADOR
compra=(total>16)

# OUTPUT
print("#######################")
print("# BOLETA DE VENTA")
print("#######################")
print("#")
print("# Cliente:  ", cliente)
print("# Mesero:  ", mesero)
print("# Item   :  ",Entrada,"  Nr de entradas")
print("# P.U.   :  S/.", pu_entradas)
print("# Total  :  S/.", total)
print("#######################")
