#INPUT
cliente=input("Ingrese el nombre del cliente:")
empresa=input("Ingrese el nombre de la empresa:")
muebles=int(input("Ingrese Nr de muebles:"))
pu_muebles=float(input("Ingrese precio unitario:"))

# PROCESSING
total = (pu_muebles* muebles)

#VERIFICADOR
compra=(total>21)

# OUTPUT
print("#######################")
print("# BOLETA DE VENTA")
print("#######################")
print("#")
print("# Cliente:  ", cliente)
print("# Empresa:  ", empresa)
print("# Item   :  ",muebles,"  Nr de muebles")
print("# P.U.   :  S/.", pu_muebles)
print("# Total  :  S/.", total)
print("#######################")
