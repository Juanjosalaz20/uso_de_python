'''
Problema: Almacenar los nombres de 3 ciudades en una tupla y luego mostrar:

    La primera y la última ciudad.

    La cantidad de caracteres de cada ciudad.
'''

C1 = input('Ingrese una ciudad: ')
C2 = input('Ingrese una ciudad diferente a la anterior: ')
C3 = input('Ingrese una ciudad diferente a la anterior: ')

Tupla = (C1, C2, C3)

print('Esta es la primera ciudad que ingresaste:',Tupla[0])
print('Esta es la ultima ciudad que ingresaste:',Tupla[2])
print('Esta es la cantidad de caracteres que tiene la primera ciudad:',len(Tupla[0]))
print('Esta es la cantidad de caracteres que tiene la segunda ciudad:',len(Tupla[1]))
print('Esta es la cantidad de caracteres que tiene la ultima ciudad:',len(Tupla[2]))