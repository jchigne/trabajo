#INPUT
cliente=input("Ingrese el nombre del cliente:")
empresa=input("Ingrese el nombre de la empresa:")
periodicos=int(input("Ingrese Nr de periodicos:"))
pu=float(input("Ingrese precio unitario:"))

# PROCESSING
total = (pu* periodicos)

#VERIFICADOR
compra=(total>25)

# OUTPUT
print("#######################")
print("# BOLETA DE VENTA")
print("#######################")
print("#")
print("# Cliente:  ", cliente)
print("# Empresa:  ", empresa)
print("# Item   :  ",periodicos,"  Nr de periodicos")
print("# P.U.   :  S/.", pu)
print("# Total  :  S/.", total)
print("#######################")
