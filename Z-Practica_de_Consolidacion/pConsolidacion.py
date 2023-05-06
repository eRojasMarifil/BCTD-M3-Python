'''
FILTRANDO DATOS

INSTRUCCIONES
Lee con atención cada uno de los requerimientos que se presentan a continuación, y desarrolla la prueba de acuerdo con lo solicitado.
DESCRIPCIÓN
Dada Ia siguiente lista de nombres:
    H                              
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
    magos={}
    for nombre, categoria, in dNombres.items():
        if categoria =='Mago':
            magos['El gran ' + nombre] = categoria
    return magos

def divisor():
    for i in range(20):
        print('_',end='')
    print(' ')
       
        
def imprimir_nombres(diccionario):
    for nombre, categoria, in diccionario.items():
        print (nombre)
        
def selector_x_categoria(categoriaPedida, diccionario): 
    categorizados={}
    print (f'Nombres que son {categoriaPedida}s:')
    if True:
        for nombre, categoria, in diccionario.items():
            if categoria==categoriaPedida:
                categorizados[nombre]=categoriaPedida
        return categorizados
    
print('Lista completa de nombres:')
imprimir_nombres(dNombres)
divisor()
print('Nombres que son Magos:')
imprimir_nombres(hacer_grandioso(dNombres))
divisor()
imprimir_nombres(selector_x_categoria('Científico',dNombres))
divisor()
imprimir_nombres(selector_x_categoria('Otro',dNombres))