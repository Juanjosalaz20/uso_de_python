'''
Problema: Crear un diccionario con las calificaciones de 3 estudiantes 
y permitir que el usuario consulte la calificación de uno de ellos.
'''
Calificaciones = {'Pepe': {'Matematicas': 4.1, 'Ciencia': 4.5, 'Quimica': 3.8}, 
                  'Laura': {'Matematicas': 4.7, 'Ciencia': 4.8, 'Quimica': 4.3},  
                  'Jose':{'Matematicas': 3.6, 'Ciencia': 4.0, 'Quimica': 4.2}}

Name = input('Ingrese el nombre del estudiante: ').title()

print(Calificaciones.get(Name, 'El estudiante no se encuentra en la lista'))



