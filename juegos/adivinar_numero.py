import random
import time
def adivinar_numero():
    cpu =  random.randint(1,10)
    usuario= int(input("Adivina el número en el que estoy pensando  entre el 1 al 10"))
    if usuario == cpu:
        print("Lo adivinaste!")
    else:
        print("Trolleaste")
    print( 'El numero era ' + str(cpu))
    time.sleep(2)
    pass
