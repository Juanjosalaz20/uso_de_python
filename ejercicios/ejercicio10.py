'''
Problema: Crear un diccionario con algunos productos 
y permitir que el usuario agregue un nuevo producto con su precio.
'''
Productos = {'Martillo': 15000, 'Cierra': 20000, 'Tornillo': 500, 'Destornillador': 8000 }

print('Productos: ', Productos)

key = input('Ingrese el nombre del producto que desea agregar: ').title()
val = input('Ingrese el valor del producto: ')

Productos.update({key : val})
print('Productos: ', Productos)