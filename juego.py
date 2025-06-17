import random

print("Bienvenido al juego piedra, papel o tijera")

while True:
    print("1 = piedra, 2 = papel, 3 = tijera")
    jugador = int(input("Elige un número (1, 2 o 3): "))

    if jugador not in [1, 2, 3]:
        print("Opción no válida. Solo puedes escribir 1, 2 o 3.")
    else:
        computadora = random.randint(1, 3)

        if jugador == 1:
            print("Tú elegiste: piedra")
        elif jugador == 2:
            print("Tú elegiste: papel")
        elif jugador == 3:
            print("Tú elegiste: tijera")

        if computadora == 1:
            print("La computadora eligió: piedra")
        elif computadora == 2:
            print("La computadora eligió: papel")
        elif computadora == 3:
            print("La computadora eligió: tijera")

        if jugador == computadora:
            print("¡Empate!")
        elif jugador == 1 and computadora == 3:
            print("¡Ganaste! Piedra aplasta a tijera.")
        elif jugador == 2 and computadora == 1:
            print("¡Ganaste! Papel envuelve a piedra.")
        elif jugador == 3 and computadora == 2:
            print("¡Ganaste! Tijera corta el papel.")
        elif jugador == 3 and computadora == 1:
            print("Perdiste. Piedra aplasta a tijera.")
        elif jugador == 1 and computadora == 2:
            print("Perdiste. Papel envuelve a piedra.")
        elif jugador == 2 and computadora == 3:
            print("Perdiste. Tijera corta el papel.")

    jugar_otra = input("¿Quieres jugar otra vez? (si/no): ")
    if jugar_otra.lower() != "si":
        print("Gracias por jugar. Fin del juego.")
        break

