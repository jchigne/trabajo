#INPUT
cliente=input("Ingrese el nombre del cliente:")
panaderia=input("Ingrese el nombre de la panaderia:")
pasteles=int(input("Ingrese Nr de pasteles:"))
pu=float(input("Ingrese precio unitario por pastel:"))

# PROCESSING
total = (pu* pasteles)

#VERIFICADOR
compra=(total>20)

# OUTPUT
print("#######################")
print("# BOLETA DE VENTA")
print("#######################")
print("#")
print("# Cliente:  ", cliente)
print("# Panaderia:  ", panaderia)
print("# Item   :  ",pasteles,"  Nr de pasteles")
print("# P.U.   :  S/.", pu)
print("# Total  :  S/.", total)
print("#######################")
