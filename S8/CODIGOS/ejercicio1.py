#Tenemos una lista de números
#[3, 5, 2, 8, 1, 10]
#Se requiere encontrar el primer número par en la lista utilizando un
#bucle while.

listaO = [3, 5, 2, 8, 1, 10]
listaR = []
i = 0

while i<len(listaO):
    if listaO[i]%2==0:
        listaR.append(listaO[i])
    i=i+1


if len(listaR)>0:
    print("El resultado es", listaR)
else:
    print("No hay número(s) par(s)")