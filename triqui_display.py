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

