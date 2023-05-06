'''
FILTRANDO DATOS

INSTRUCCIONES
Lee con atención cada uno de los requerimientos que se presentan a continuación, y desarrolla la prueba de acuerdo con lo solicitado.
DESCRIPCIÓN
Dada Ia siguiente lista de nombres:
    Harry Houdini
    Newton
    David Blaine
    Hawking
    Messi
    Teller
    Einstein
    pele
    Juanes
Y sabiendo que Harry Houdini, David Blaine y Teller son magos. Y también que Newton, Hawking y Einstein son científicos. Debemos separar los nombres en tres grupos: magos, científicos y otros; y escribir una función llamada hacer_grandioso(), que modifique la lista de magos añadiendo la frase ‘El gran‘ antes del nombre de cada mago.
Crear una función llamada lista imprimir_nombres(), que imprime el nombre de cada persona de la lista.
Finalmente, imprimir en pantalla la lista completa de nombres antes de ser modificados; luego imprimir los nombres de los magos grandiosos, los nombres de los científicos, y los restantes.
'''
dNombres = {'Harry Houdini':'Mago',
           'Newton':'Científico',
           'David Blaine':'Mago',
           'Hawking':'Científico',
           'Messi':'Otro',
           'Teller':'Mago', 
           'Einstein':'Científico',
           'pele':'Otro',
           'Juanes':'Otro'}

def hacer_grandioso(dNombres):
    for nombre, categoria, in dNombres.items():
        if categoria =='Mago':
            dNombres[nombre] = 'El gran' + nombre
    return hacer_grandioso

print('Lista completa de nombres:')
for nombre, categoria, in dNombres.items():
    print (nombre)