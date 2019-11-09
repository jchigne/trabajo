#INPUT
cliente=input("Ingrese el nombre del cliente:")
empresa=input("Ingrese el nombre de la empresa:")
sillas=int(input("Ingrese Nr de sillas:"))
pu_sillas=float(input("Ingrese precio unitario:"))

# PROCESSING
total = (pu_sillas* sillas)

#VERIFICADOR
compra=(total>31)

# OUTPUT
print("#######################")
print("# BOLETA DE VENTA")
print("#######################")
print("#")
print("# Cliente:  ", cliente)
print("# Empresa:  ", empresa)
print("# Item   :  ",sillas,"  Nr de sillas")
print("# P.U.   :  S/.", pu_sillas)
print("# Total  :  S/.", total)
print("#######################")
