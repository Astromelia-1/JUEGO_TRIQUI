from triqui_game import TriquiGame
from triqui_display import TriquiDisplay
from triqui_score import TriquiScore
from triqui_players import TriquiPlayers

def main():
    score_manager = TriquiScore()
    display = TriquiDisplay()
    players = TriquiPlayers()
    nombre1, nombre2 = players.pedir_nombres()  # <-- ¡Sólo esta vez!

    while True:
        display.limpiar_pantalla()
        print("╔══════════════════════╗")
        print("║     JUEGO TRIQUI     ║")
        print("╚══════════════════════╝")
        players.mostrar_jugadores()
        print("\n1. Jugar una partida")
        print("2. Ver historial de partidas")
        print("3. Salir")

        opcion = input("Selecciona una opción (1/2/3): ")
        if opcion == "1":
            game = TriquiGame(players.nombre1, players.nombre2, display, score_manager)
            game.jugar()
        elif opcion == "2":
            score_manager.mostrar_historial()
        elif opcion == "3":
            print("¡Hasta pronto! 👋")
            break
        else:
            print("Opción no válida. Intenta de nuevo.")

if __name__ == "__main__":
    main()

import os
from typing import List

class TriquiDisplay:
    def limpiar_pantalla(self) -> None:
        os.system("cls" if os.name == "nt" else "clear")

    def mostrar_tablero(self, tablero: List[List[str]]) -> None:
        print("\n   1   2   3")
        for i, fila in enumerate(tablero):
            print(" +---+---+---+")
            print(f"{i + 1}|", end="")
            for celda in fila:
                print(f" {celda if celda != ' ' else ' '} |", end="")
            print()
        print(" +---+---+---+\n")


