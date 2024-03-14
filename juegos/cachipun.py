import random
import time
def cachipun():
    """
    Esta función representa el juego de cachipun.
    Debes pedir al usuario que elija piedra, papel o tijera, y luego comparar su elección con la de la computadora.
    La computadora debe elegir una opción al azar.
    """
    while True:
        OBJ = input("Eliga 'Piedra', 'Papel' o 'Tijera'\n")
        if OBJ.lower() == 'piedra':
            OBJ = 'Piedra'
            break
        elif OBJ.lower() == 'papel':
            OBJ = 'Papel'
            break
        elif OBJ.lower() == 'tijera':
            OBJ = 'Tijera'
            break
        else:
            print('Ha ocurrido un error, intente nuevamente')


    Enemy_OBJ_num = random.randint(1,3)

    if Enemy_OBJ_num == 1:
        Enemy_OBJ = "Piedra"
    elif Enemy_OBJ_num == 2:
        Enemy_OBJ = "Papel"
    elif Enemy_OBJ_num == 3:
        Enemy_OBJ = "Tijera"

    Winner = 'None'

    print('CA')
    time.sleep(1)
    print('CHI')
    time.sleep(1)
    print('PUN')
    time.sleep(1)
    print(f"   Tú      Computadora")
    print(f"'{OBJ}' vs '{Enemy_OBJ}'")
    time.sleep(2)

    if Enemy_OBJ == OBJ:
        Winner = 'Empate'
    elif Enemy_OBJ == 'Piedra' and OBJ == "Tijera":
        Winner = 'Computadora'
    elif Enemy_OBJ == 'Papel' and OBJ == "Piedra":
        Winner = 'Computadora'
    elif Enemy_OBJ == 'Tijera' and OBJ == "Papel":
        Winner = 'Computadora'
    elif OBJ == 'Piedra' and Enemy_OBJ == "Tijera":
        Winner = 'Player'
    elif OBJ == 'Papel' and Enemy_OBJ == "Piedra":
        Winner = 'Player'
    elif OBJ == 'Tijera' and Enemy_OBJ == "Papel":
        Winner = 'Player'

    if Winner == "None":
        print('Ha ocurrido un error, intente nuevamente')
    elif Winner == "Empate":
        print("Es un empate")
    elif Winner == "Player":
        print("¡HAS GANADO!")
    elif Winner == "Computadora":
        print("Has perdido :c")

    time.sleep(2)
    
    pass