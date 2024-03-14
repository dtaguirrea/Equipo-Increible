import random
def adivinar_numero():
    cpu =  random.randint(1,10)
    usuario= input("Adivina el número en el que estoy pensando ")
    if usuario == cpu:
        print("Lo adivinaste!")
    else:
        print("Trolleaste")
    pass
adivinar_numero()