#Se tiene la siguiente lista de números:
#numeros = [3, 5, 2, 8, 1, 10]
#Calcular la suma de todos los números de la lista utilizando un bucle
#while.

numeros = [3, 5, 2, 8, 1, 10]
i=0
suma=0

while i<len(numeros):
    suma = suma + numeros[i]
    i=i+1
print(f"La suma de los números es: {suma}")