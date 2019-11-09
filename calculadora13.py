#calculadora nro13
#Esta calculadora realiza el calculo de la producion

#Declaracion de datos
costo_fijo2,costo_fijo_medio,producion=0.0,0.0,0.0

#calculadora
costo_fijo2=2000
costo_fijo_medio=100
producion=(costo_fijo2/costo_fijo_medio)
verificador=(producion==20)

#mostrar datos
print("costo fijo2=",costo_fijo2)
print("costo fijo medio=",costo_fijo_medio)
print("producion =",producion)
print("producion==20",verificador)
