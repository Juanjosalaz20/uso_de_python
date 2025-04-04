'''Solicitar una edad y clasificarla
 en menores de edad (0-17), adultos (18-64) y 
 adultos mayores (65+)
 Para este ejercicio usar if elif else
 y tambien usar match/case
 '''
minor = range(0,18)
adult = range(18,65)

age = int(input('Ingrese su edad: '))

#With if
#Puedo incluir los rangos dentro del mismo if y asi evitar definir las variables
if age in minor:
    print('Eres menor de edad')
elif age in adult:
    print('Eres mayor de edad')
else:
    print('Eres un adulto mayor')