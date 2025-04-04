dia = input('Ingrese el dia de la semana: ')
match dia:
    case 'sabado' | 'domingo':
        print(f'{dia} es fin de semana')
    case 'lunes':
        print(f'{dia} es el dia mas dificil')
    case 'martes' | 'miercoles' | 'jueves':
        print(f'{dia} es un dia normal')
    case _:
        print(f'No ingresaste un dia de la semana')
