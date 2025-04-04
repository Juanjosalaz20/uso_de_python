print('Ingrese el nombre de los jugadores')
Name_p1 = input('Jugardor 1: ').title()
Name_p2 = input('Jugardor 2: ').title()

moves = ('piedra', 'papel', 'tijera')
print('A continuacion eligan entre', moves)

score_p1 = 0
score_p2 = 0


while score_p1 < 2 and score_p2 < 2:
    p1_move = input(f'{Name_p1} ingresa tu eleccion: ').lower()
    while p1_move not in moves:
        p1_move = input(f'{Name_p1} tu eleccion no es valida, intenta de nuevo: ').lower()

    p2_move = input(f'{Name_p2} ingresa tu eleccion: ').lower()

    while p2_move not in moves:
        p2_move = input(f'{Name_p2} tu eleccion no es valida, intenta de nuevo: ').lower()

    if p1_move == p2_move:
        print ('Empate')
    elif p1_move == moves[0] and p2_move == moves[2] or \
        p1_move == moves[1] and p2_move == moves[0] or \
        p1_move == moves[2] and p2_move == moves[1]:
        print('Gana', Name_p1)
        score_p1 += 1
    else:
        print('Gana', Name_p2)
        score_p2 += 1
    print('-'*30)

if score_p1 == 2:
    print('-'*30)
    print(f'El ganador es {Name_p1}')
else:
    
    print(f'El ganador es {Name_p2}')
    