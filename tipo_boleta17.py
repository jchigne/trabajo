#INPUT
cliente=input("Ingrese el nombre del cliente:")
ferreteria=input("Ingrese el nombre de la ferreteria:")
cemento=int(input("Ingrese Nr de bolsas de cemento:"))
pu=float(input("Ingrese precio unitario por bolsa:"))

# PROCESSING
total = (pu* cemento)

#VERIFICADOR
compra=(total>17)

# OUTPUT
print("#######################")
print("# BOLETA DE VENTA")
print("#######################")
print("#")
print("# Cliente:  ", cliente)
print("# Ferreteria:  ", ferreteria)
print("# Item   :  ",cemento,"  Nr de bolsas")
print("# P.U.   :  S/.", pu)
print("# Total  :  S/.", total)
print("#######################")
