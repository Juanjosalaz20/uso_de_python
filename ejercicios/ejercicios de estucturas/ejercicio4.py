'''
Problema: Escribe un programa que determine si un número ingresado por el 
usuario es par o impar utilizando el operador módulo %.
'''
N1 = int(input('Ingrese un número: '))

Módulo = N1 % 2

Par = Módulo == 0

if Par == False:
    print('Su numero no es par')
else:
    print('Su numero es par')
