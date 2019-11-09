#INPUT
cliente=input("Ingrese el nombre del cliente:")
pantalones=int(input("Ingrese Nr de pantalones:"))
pu_pantalones=float(input("Ingrese precio uninitario de pantalones:"))

# PROCESSING
total = (pu_pantalones*pantalones)

#VERIFICADOR
compra=(total>1)

# OUTPUT
print("#######################")
print("# BOLETA DE VENTA")
print("#######################")
print("#")
print("# Cliente:  ", cliente)
print("# Item   :  ",pantalones,"  Nr de pantalones")
print("# P.U.   :  S/.", pu_pantalones)
print("# Total  :  S/.", total)
print("#######################")
