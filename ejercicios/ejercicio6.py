'''
Problema: Solicitar al usuario 5 números enteros, almacenarlos en una lista y luego mostrar:

    La lista original.

    La lista en orden inverso.

    La suma de los números.
'''

N1 = int(input('Ingrese un numero entero: '))
N2 = int(input('Ingrese otro numero entero: '))
N3 = int(input('Ingrese otro numero entero: '))
N4 = int(input('Ingrese otro numero entero: '))
N5 = int(input('Ingrese otro numero entero: '))

Lista = [N1,N2,N3,N4,N5]
print(Lista)

Lista.reverse()
print(Lista)

print(sum(Lista))