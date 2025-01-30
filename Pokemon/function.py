import random


# Función para mostrar el menú principal
def menuPrincipal(poke: list[str]):
    while True:
        print("---------------------------------------------------")
        print("====== MENU PRINCIPAL POKE ======")
        print("1. Jugar")
        print("2. Elección Pokes")
        print("3. Lista Pokes")
        print("0. Salir")

        try:
            eleccion = int(input("Ingrese la opción: "))
        except ValueError:
            print("Por favor, ingresa un número válido.")
            continue

        match eleccion:
            case 1:
                jugador = jugadorPoke(poke)
                maquina = maquinaPoke(poke)
                habilidadesJugador = habilidades(jugador)
                habilidadesMaquina = habilidades(maquina)
                print("Tu equipo:")
                for p in habilidadesJugador:
                    print(p)
                print("Equipo de la máquina:")
                for p in habilidadesMaquina:
                    print(p)
                combate(jugador, maquina, habilidadesJugador, habilidadesMaquina)
            case 2:
                jugador = jugadorPoke(poke)
                maquina = maquinaPoke(poke)
                print("Tu elección para el combate es:", jugador)
                print("---------------------------------------------------")
                print("La elección de la máquina para el combate es:", maquina)
                print("---------------------------------------------------")

                habilidadesJugador = habilidades(jugador)
                habilidadesMaquina = habilidades(maquina)

                print("Tus habilidades:")
                for p in habilidadesJugador:
                    print(p)

                print("Habilidades de la máquina:")
                for p in habilidadesMaquina:
                    print(p)
            case 3:
                print("---------------------------------------------------")
                print("La lista de Pokes es:")
                print(poke)
                print(habilidades(poke))
            case 0:
                print("Saliendo del juego...")
                break
            case _:
                print("Opción no válida, por favor elige otra.")


# Función para definir las habilidades de cada Pokémon
def habilidades(poke: list[str]) -> list[dict]:
    habilidades_por_poke = []
    for i in poke:
        if i == "Gomi":
            ataques = ["Pedo pestoso", "Wiskey al trago", "Clase de fol"]
            curas = ["Cafe", "+Aura"]
        elif i == "Chori":
            ataques = ["Guantazo", "Pedo pestoso", "Aliento mañanero"]
            curas = ["+Vida"]
        elif i == "Morci":
            ataques = ["Pedo pestoso", "Wiskey al trago", "Clase de fol"]
            curas = ["Cafe", "+Vida"]
        elif i == "Beer":
            ataques = ["Guantazo", "Puñetazo", "Clase de fol"]
            curas = ["+Aura", "+Vida", "Cafe"]
        elif i == "Tonic":
            ataques = ["Wiskey al trago", "Puñetazo"]
            curas = ["+Aura", "+Vida", "Cafe"]
        else:
            ataques = ["Wiskey al trago", "Puñetazo"]
            curas = ["+Aura"]

        habilidades_por_poke.append({"Pokemon": i, "Ataques": ataques, "Curas": curas})

    return habilidades_por_poke


# Función para que el jugador elija Pokémon
def jugadorPoke(poke: list[str]) -> list[str]:
    jugadorPokes = []
    print("---------------------------------------------------")
    print("Elige tus Pokes para el combate (3 máximo):")
    print(poke)
    while len(jugadorPokes) < 3:
        eleccion = input("Introduce el nombre de tu Pokémon: ").strip()
        if eleccion not in poke:
            print("Ese Pokémon no está en la lista, elige otro.")
        elif eleccion in jugadorPokes:
            print("Ya has elegido ese Pokémon, elige otro.")
        else:
            jugadorPokes.append(eleccion)
            print(f"{eleccion} añadido a tu equipo.")
    return jugadorPokes


# Función para que la máquina elija Pokémon
def maquinaPoke(poke: list[str]) -> list[str]:
    maquinaPokes = random.sample(poke, 3)
    print("La máquina ha elegido sus Pokémon.")
    return maquinaPokes


def combate(jugador: list[str], maquina: list[str], habilidadesJugador: list[dict], habilidadesMaquina: list[dict]):
    print("---------------------------------------------------")
    print("¡Comienza el combate!")

    # Inicializar vida de los Pokémon
    vida_jugador = {poke["Pokemon"]: 100 for poke in habilidadesJugador}
    vida_maquina = {poke["Pokemon"]: 100 for poke in habilidadesMaquina}

    turno = True  # True: Turno del jugador, False: Turno de la máquina
    ultima_accion_jugador = None  # Guardar la última acción del jugador
    ultima_accion_maquina = None  # Guardar la última acción de la máquina

    # Mientras haya Pokémon vivos en ambos equipos
    while any(v > 0 for v in vida_jugador.values()) and any(v > 0 for v in vida_maquina.values()):
        if turno:
            # Turno del jugador
            print("\nTu turno:")
            print("Tus Pokémon vivos:")
            for poke, vida in vida_jugador.items():
                if vida > 0:
                    print(f"{poke} (HP: {vida})")

            print("\nPokémon vivos de la máquina:")
            for poke, vida in vida_maquina.items():
                if vida > 0:
                    print(f"{poke} (HP: {vida})")

            # Elegir acción
            if ultima_accion_jugador != "curar":
                accion = input("¿Qué deseas hacer? (1. Atacar, 2. Curar): ").strip()
            else:
                accion = "1"  # Si curó en el turno anterior, forzar a atacar

            if accion == "1":
                # Atacar
                atacante = input("Elige un Pokémon para atacar: ").strip()
                if atacante not in vida_jugador or vida_jugador[atacante] <= 0:
                    print("Elige un Pokémon válido que esté vivo.")
                    continue

                objetivo = input("Elige un Pokémon de la máquina para atacar: ").strip()
                if objetivo not in vida_maquina or vida_maquina[objetivo] <= 0:
                    print("Elige un Pokémon válido que esté vivo en el equipo de la máquina.")
                    continue

                ataque = random.choice([p["Ataques"] for p in habilidadesJugador if p["Pokemon"] == atacante][0])
                dano = random.randint(10, 30)
                vida_maquina[objetivo] -= dano
                vida_maquina[objetivo] = max(0, vida_maquina[objetivo])  # No puede ser menor a 0
                print(f"{atacante} usó {ataque} contra {objetivo} y causó {dano} de daño.")
                ultima_accion_jugador = "atacar"
            elif accion == "2":
                # Curar
                if ultima_accion_jugador == "curar":
                    print("No puedes curar dos rondas seguidas. Pierdes tu turno.")
                    ultima_accion_jugador = "atacar"  # Forzar al siguiente turno que ataque
                    continue

                curador = input("Elige un Pokémon para curar: ").strip()
                if curador not in vida_jugador or vida_jugador[curador] <= 0:
                    print("Elige un Pokémon válido que esté vivo.")
                    continue

                cura = random.choice([p["Curas"] for p in habilidadesJugador if p["Pokemon"] == curador][0])
                cantidad_curada = random.randint(10, 30)
                vida_jugador[curador] += cantidad_curada
                vida_jugador[curador] = min(100, vida_jugador[curador])  # No puede superar 100
                print(f"{curador} usó {cura} y recuperó {cantidad_curada} puntos de vida.")
                ultima_accion_jugador = "curar"
            else:
                print("Opción no válida. Pierdes tu turno.")
                ultima_accion_jugador = "atacar"
        else:
            # Turno de la máquina
            print("\nTurno de la máquina:")
            if ultima_accion_maquina == "curar":
                # Si la máquina curó en la ronda anterior, no puede curar esta ronda
                accion_maquina = "atacar"
            else:
                accion_maquina = random.choice(["atacar", "curar"])

            if accion_maquina == "atacar":
                atacante = random.choice([poke for poke, vida in vida_maquina.items() if vida > 0])
                objetivo = random.choice([poke for poke, vida in vida_jugador.items() if vida > 0])
                ataque = random.choice([p["Ataques"] for p in habilidadesMaquina if p["Pokemon"] == atacante][0])
                dano = random.randint(10, 30)
                vida_jugador[objetivo] -= dano
                vida_jugador[objetivo] = max(0, vida_jugador[objetivo])  # No puede ser menor a 0
                print(f"{atacante} usó {ataque} contra {objetivo} y causó {dano} de daño.")
                ultima_accion_maquina = "atacar"
            elif accion_maquina == "curar":
                curador = random.choice([poke for poke, vida in vida_maquina.items() if vida > 0])
                cura = random.choice([p["Curas"] for p in habilidadesMaquina if p["Pokemon"] == curador][0])
                cantidad_curada = random.randint(10, 30)
                vida_maquina[curador] += cantidad_curada
                vida_maquina[curador] = min(100, vida_maquina[curador])  # No puede superar 100
                print(f"{curador} usó {cura} y recuperó {cantidad_curada} puntos de vida.")
                ultima_accion_maquina = "curar"

        turno = not turno  # Cambiar turno

    # Determinar ganador
    print("\nFin del combate:")
    if any(v > 0 for v in vida_jugador.values()):
        print("¡Felicidades, ganaste!")
    else:
        print("La máquina ha ganado.")
