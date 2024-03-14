def memoria():
    import random
    import time
    """
    Esta función representa el juego de memoria.
    Debes generar una secuencia de números al azar y mostrarla al usuario.
    Luego, debes pedir al usuario que repita la secuencia.
    Se debe mostrar un mensaje si el usuario acierta o no.
    """
    input('presione enter para empezar el juego')

    print('Cuantos numeros quieres memorizar?')
    num = int(input(''))

    i = 0
    tot = ''

    while i < num:
        dig = str(random.randint(0,9))
        tot += dig

        i += 1
    print(tot)
    
    input('Te lo aprendiste?')

    i = 0
    while i < 1000:
        print('\n')
        i += 1

    print('agrega el numero :)')
    us = str(input(''))

    if us == tot:
        print('Buena memoria!')
        return 1
    else:
        print('No es el numero, F')
        return 0



    
