import random

# juego de piedra, papel o tijera
print("Bienvenido al juego piedra, papel o tijera")
print("1 = piedra, 2 = papel, 3 = tijera")

# jugador escoge una opción
jugador = int(input("Elige un número (1, 2 o 3): "))

# computadora escoge automáticamente
computadora = random.randint(1, 3)

# mostrar elecciones
if jugador == 1:
    print("Tú elegiste: piedra")
elif jugador == 2:
    print("Tú elegiste: papel")
elif jugador == 3:
    print("Tú elegiste: tijera")
else:
    print("Opción no válida.")

if computadora == 1:
    print("La computadora eligió: piedra")
elif computadora == 2:
    print("La computadora eligió: papel")
elif computadora == 3:
    print("La computadora eligió: tijera")

# comparar resultados
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


print("Fin del juego")