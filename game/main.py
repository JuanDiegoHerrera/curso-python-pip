import random
# supuestamente con alt + z se puede usar un renglon en 2 osea hacer espacio y uqe sea un renglon, esto es otra cosa
print(" Bienvenido")
juagador1 = input( " introdusca el nombre de jugador 1  ")
print (" piedra = 1.-, papel = 2, tijera = 3 ")
piedra = 1
papel = 2
tijera = 3

jugador2 = " computadora "
eleccion1 = (0)
eleccion2 = (0)
contador = (0)

# si te da negativo gana jugador2 , la comu, si te da positivo gana el jugador1

while int(contador) == 0:
    eleccion1 = input( " seleccone piedra(1), papel(2) o tijera(3) ")
    eleccion2 = random.randint(1, 3)
    if int(eleccion1) == 1 and eleccion2 == 3:
       eleccion1 = 5
       print(" ganador "+ juagador1)
    elif int(eleccion1) == 3 and eleccion2 ==3:
        eleccion2 = 5
        #aca le pongo que las elecciones cambian a 5 para que su valor sea mayor al de tijera
        print(" ganador " + jugador2)
    else:
        if int(eleccion1) > eleccion2 :
            print(" el ganador es " + juagador1)

        elif int(eleccion1) < eleccion2 :
            print( " el ganador es  " + jugador2 )

        elif int(eleccion1) == eleccion2 :
            print(" empate")


    contador = input(" si desea seguir jugando aprete 0, si no, aprete otra tecla ")