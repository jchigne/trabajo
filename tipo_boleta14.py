#INPUT
cliente=input("Ingrese el nombre del cliente:")
grifo=input("Ingrese el nombre del grifo:")
petroleo=int(input("Ingrese Nr de galones de petroleo:"))
pu=float(input("Ingrese precio unitario por galon:"))

# PROCESSING
total = (pu* petroleo)

#VERIFICADOR
compra=(total>14)

# OUTPUT
print("#######################")
print("# BOLETA DE VENTA")
print("#######################")
print("#")
print("# Cliente:  ", cliente)
print("# Grifo:  ", grifo)
print("# Item   :  ",petroleo,"  galones de petroleo")
print("# P.U.   :  S/.", pu)
print("# Total  :  S/.", total)
print("#######################")
