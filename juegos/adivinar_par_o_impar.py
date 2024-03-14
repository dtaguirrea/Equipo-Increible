def adivinar_par_o_impar():
    import time
    print("Si quieres jugar par o impar, di ""Es hora de ser heroe""")
    respuesta=input()
    if respuesta!="Es hora de ser heroe":
        print("bueno pues :(")
        time.sleep(1)
        return()
    if respuesta=="Es hora de ser heroe":
        print("¿Será par o impar?")
        adivina=input()
        while adivina !="par" and adivina != "impar":
            print("Chistoso, pero no tanto")
            print("¿Será par o impar?")
            adivina=input()
        print("La ruleta esta girando")
    import random
    par_impar=""
    numero = False
    numero_random= random.randint(-999,999)
    if numero_random/2==numero_random//2:
        par_impar="par"
    else:
        par_impar="impar"
    if numero_random==par_impar:
        numero = True
    print("A salido", numero_random, "que es", par_impar)
    if par_impar==adivina:
        print("Adivinaste")
    else:
        print("Manqueque")
    time.sleep(2)

    
