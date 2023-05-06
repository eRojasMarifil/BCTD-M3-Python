#Tienes la siguiente lista de números:[45, 23, 67, 89, 12, 56, 78, 90]
#Encontrar el número más rande en la lista utilizando un bucle for.

numeros = [45, 23, 67, 90, 12, 56, 78, 89]

numM=numeros[0]

for i in numeros:
    if i > numM:
        numM=i
print(numM)