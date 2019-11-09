#INPUT
cliente=input("Ingrese el nombre del cliente:")
empresa=input("Ingrese el nombre de la empresa:")
televisores=int(input("Ingrese Nr de televisores:"))
pu=float(input("Ingrese precio unitario:"))

# PROCESSING
total = (pu* televisores)

#VERIFICADOR
compra=(total>13)

# OUTPUT
print("#######################")
print("# BOLETA DE VENTA")
print("#######################")
print("#")
print("# Cliente:  ", cliente)
print("# Empresa:  ", empresa)
print("# Item   :  ",televisores,"  Nr de televisores")
print("# P.U.   :  S/.", pu)
print("# Total  :  S/.", total)
print("#######################")
