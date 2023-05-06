"""
De la siguiente lista de precios de productos:
[25.50, 12.30, 36.40, 9.75, 15.20]
Calcular el precio total de la compra con un descuento del 10%.
"""

precios=[25500, 12300, 36400, 9750, 15200]
suma=0
total=0
i=0

while i<len(precios):
    suma=suma+precios[i]
    i=i+1

total=suma*0.9

print(f"Su total es {suma}, pero con descuento es {total}")
