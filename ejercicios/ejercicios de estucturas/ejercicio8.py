'''Problema: Solicitar al usuario dos conjuntos de números y luego mostrar:

    La unión de ambos conjuntos.

    La intersección de ambos conjuntos'''
    
Conjunto1 = set(map(int,input('Ingrese un conjunto de numeros: ').split()))
Conjunto2 = set(map(int,input('Ingrese otro conjunto de numeros: ').split()))

print('Esta es la union de los dos conjuntos:', Conjunto1|Conjunto2) 
print('Esta es la interseccion de ambos conjuntos:', Conjunto1 & Conjunto2)