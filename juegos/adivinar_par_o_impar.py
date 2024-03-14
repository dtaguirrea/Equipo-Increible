def adivinar_par_o_impar(numero):
    import random
    par_impar=""
    numero_random= random.randint(-999,999)
    if numero_random/2==numero_random//2:
        par_impar="par"
    else:
        par_impar="impar"
    if numero==par_impar:
        numero=True
    print("A salido", numero_random, "que es", par_impar)
    if numero==True:
        return ("Adivinaste")
    else:
        return ("Manqueque")
print("Si quieres jugar par o impar, di ""Es hora de ser heroe""")
respuesta=input()
if respuesta!="Es hora de ser heroe":
    print("bueno pues :(")
if respuesta=="Es hora de ser heroe":
    print("¿Será par o impar?")
    adivina=input()
    while adivina !="par" and adivina != "impar":
        print("Chistoso, pero no tanto")
        print("¿Será par o impar?")
        adivina=input()
    print("La ruleta esta girando")
    print(adivinar_par_o_impar(adivina))
    
