

def juego_del_dado():
    import random

    """
    Esta función tiene que pedirle al usuario que aprete enter para que lance un dado.
    Esto genera un número al azar que se le suma a la puntuación del usuario.
    Después el computador también tiene que lanzar un dado.
    El primero en sumar 30 puntos gana.

    """
    puntuación_1 = 0
    puntuación_2 = 0
    
    while (puntuación_1 < 30) and (puntuación_2 < 30):
        input('presione enter para lanzar el dado')
        
        puntuación_1 += random.randint(1,6)
        print('Su puntuación es ' + str(puntuación_1))

        if puntuación_1 < 30:
            puntuación_2 += random.randint(1,6)
            print('La puntuación de la casa es ' + str(puntuación_2))
        
    
    if puntuación_1 >= 30:
        print('Has ganado!!')
        return 1
    else:
        print('Has perdido :(')
        return 0
    
