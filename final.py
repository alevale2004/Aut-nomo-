import random

# Variables globales para estadísticas
resultados = []
estadisticas = {
    "Jugador 1": {"ganadas": 0, "perdidas": 0, "empates": 0},
    "Jugador 2": {"ganadas": 0, "perdidas": 0, "empates": 0}
}

def mostrar_menu_principal():
    print("\n--- MENÚ PRINCIPAL ---")
    print("1. Jugar")
    print("2. Reglas del juego")
    print("3. Salir del juego")

def mostrar_reglas():
    print("\n--- REGLAS DEL JUEGO ---")
    print("Piedra vence a Tijera")
    print("Tijera vence a Papel")
    print("Papel vence a Piedra")
    print("Puedes jugar contra la computadora o contra otro jugador.")
    print("Las estadísticas se muestran al final del conjunto de partidas.")

def menu_jugar():
    while True:
        print("\n--- MODO DE JUEGO ---")
        print("1. Contra la computadora")
        print("2. Multijugador (2 jugadores)")
        print("3. Ver estadísticas de la última partida")
        print("4. Regresar al menú principal")
        opcion = input("Elige una opción (1-4): ")

        if opcion == "1":
            jugar_vs_computadora()
        elif opcion == "2":
            jugar_multijugador()
        elif opcion == "3":
            mostrar_estadisticas()
        elif opcion == "4":
            break
        else:
            print("Opción no válida. Intenta de nuevo.")

def pedir_opcion(jugador):
    while True:
        print(f"{jugador}, elige una opción:")
        print("1. Piedra")
        print("2. Papel")
        print("3. Tijera")
        eleccion = input("Tu elección (1, 2 o 3): ")
        if eleccion in ["1", "2", "3"]:
            return int(eleccion)
        else:
            print("Opción inválida. Intenta nuevamente.")

def determinar_resultado(j1, j2):
    if j1 == j2:
        return "empate"
    elif (j1 == 1 and j2 == 3) or (j1 == 2 and j2 == 1) or (j1 == 3 and j2 == 2):
        return "jugador1"
    else:
        return "jugador2"

def nombre_opcion(num):
    return ["Piedra", "Papel", "Tijera"][num - 1]

def jugar_vs_computadora():
    global resultados, estadisticas
    jugador1 = input("Ingresa tu nombre: ")
    jugador2 = "Computadora"
    limpiar_estadisticas(jugador1, jugador2)
    modo_juego(jugador1, jugador2, contra_pc=True)

def jugar_multijugador():
    global resultados, estadisticas
    jugador1 = input("Nombre del jugador 1: ")
    jugador2 = input("Nombre del jugador 2: ")
    limpiar_estadisticas(jugador1, jugador2)
    modo_juego(jugador1, jugador2, contra_pc=False)

def limpiar_estadisticas(j1, j2):
    global resultados, estadisticas
    resultados = []
    estadisticas = {
        j1: {"ganadas": 0, "perdidas": 0, "empates": 0},
        j2: {"ganadas": 0, "perdidas": 0, "empates": 0}
    }

def modo_juego(j1, j2, contra_pc):
    definir = input("¿Deseas definir el número de partidas? (si/no): ").lower()
    if definir == "si":
        try:
            n = int(input("¿Cuántas partidas deseas jugar?: "))
            for i in range(n):
                jugar_partida(j1, j2, contra_pc)
        except:
            print("Número inválido.")
    else:
        while True:
            jugar_partida(j1, j2, contra_pc)
            seguir = input("¿Deseas jugar otra partida? (si/no): ").lower()
            if seguir != "si":
                break
    mostrar_estadisticas()

def jugar_partida(j1, j2, contra_pc):
    print("\n--- NUEVA PARTIDA ---")
    jug1 = pedir_opcion(j1)
    if contra_pc:
        jug2 = random.randint(1, 3)
        print(f"{j2} eligió: {nombre_opcion(jug2)}")
    else:
        print(f"{j2}, no mires la pantalla.")
        jug2 = pedir_opcion(j2)

    print(f"{j1} eligió: {nombre_opcion(jug1)}")

    resultado = determinar_resultado(jug1, jug2)

    if resultado == "empate":
        print("¡Empate!")
        estadisticas[j1]["empates"] += 1
        estadisticas[j2]["empates"] += 1
        resultados.append(f"{j1} empató - {j2} empató")
    elif resultado == "jugador1":
        print(f"¡{j1} ganó!")
        estadisticas[j1]["ganadas"] += 1
        estadisticas[j2]["perdidas"] += 1
        resultados.append(f"{j1} ganó - {j2} perdió")
    else:
        print(f"¡{j2} ganó!")
        estadisticas[j2]["ganadas"] += 1
        estadisticas[j1]["perdidas"] += 1
        resultados.append(f"{j1} perdió - {j2} ganó")

def mostrar_estadisticas():
    if not resultados:
        print("No hay estadísticas recientes.")
        return
    print("\n--- RESUMEN DE PARTIDAS ---")
    print(f"Número total de partidas: {len(resultados)}")
    for i, r in enumerate(resultados, 1):
        print(f"Partida {i}: {r}")
    print("\n--- ESTADÍSTICAS ---")
    for jugador, datos in estadisticas.items():
        print(f"{jugador}: ganó {datos['ganadas']}, perdió {datos['perdidas']}, empató {datos['empates']}")

# Inicio del programa
while True:
    mostrar_menu_principal()
    opcion = input("Elige una opción (1-3): ")
    if opcion == "1":
        menu_jugar()
    elif opcion == "2":
        mostrar_reglas()
    elif opcion == "3":
        print("¡Gracias por jugar! Hasta luego.")
        break
    else:
        print("Opción inválida.")
