import random
def adivinar_numero():
    cpu =  random.randint(1,10)
    usuario= int(input("Adivina el número en el que estoy pensando "))
    if usuario == cpu:
        print("Lo adivinaste!")
    else:
        print("Trolleaste")
    pass
