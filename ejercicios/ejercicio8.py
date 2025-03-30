'''Problema: Solicitar al usuario dos conjuntos de números y luego mostrar:

    La unión de ambos conjuntos.

    La intersección de ambos conjuntos'''
    
Conjunto1 = set(input('Ingrese un conjunto de numeros: '))
Conjunto2 = set(input('Ingrese otro conjunto de numeros: '))

print('Esta es la union de los dos conjuntos:', Conjunto1|Conjunto2) 
print('Esta es la interseccion de ambos conjuntos:', Conjunto1 & Conjunto2)