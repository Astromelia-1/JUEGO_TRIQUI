from typing import List, Tuple

class TriquiGame:
    def __init__(self, nombre1: str, nombre2: str, display, score_manager):
        self.nombre1 = nombre1
        self.nombre2 = nombre2
        self.display = display
        self.score_manager = score_manager
        self.tablero = self.inicializar_tablero()
        self.simbolos = {self.nombre1: "X", self.nombre2: "O"}
        self.turno = self.nombre1  # Empieza el Jugador 1

    def inicializar_tablero(self) -> List[List[str]]:
        return [[" " for _ in range(3)] for _ in range(3)]

    def pedir_jugada(self) -> Tuple[int, int]:
        while True:
            try:
                mov = input(f"{self.turno}, ingresa tu jugada (fila,columna): ")
                fila, col = map(int, mov.strip().split(","))
                if not (1 <= fila <= 3 and 1 <= col <= 3):
                    print("⚠️  Ingresa números del 1 al 3 (ejemplo: 2,3)")
                    continue
                if self.tablero[fila - 1][col - 1] != " ":
                    print("⚠️  Esa casilla ya está ocupada.")
                    continue
                return fila - 1, col - 1
            except Exception:
                print("⚠️  Ingresa la jugada como: fila,columna (ejemplo: 1,3)")

    def hay_ganador(self, simbolo: str) -> bool:
        t = self.tablero
        # Filas, columnas, diagonales
        if any(all(c == simbolo for c in fila) for fila in t):
            return True
        if any(all(t[f][c] == simbolo for f in range(3)) for c in range(3)):
            return True
        if all(t[i][i] == simbolo for i in range(3)):
            return True
        if all(t[i][2 - i] == simbolo for i in range(3)):
            return True
        return False

    def tablero_lleno(self) -> bool:
        return all(c != " " for fila in self.tablero for c in fila)

    def jugar(self):
        self.display.limpiar_pantalla()
        self.tablero = self.inicializar_tablero()
        self.turno = self.nombre1

        while True:
            print(f"Turno de {self.turno} ({self.simbolos[self.turno]})")
            self.display.mostrar_tablero(self.tablero)

            fila, col = self.pedir_jugada()
            self.tablero[fila][col] = self.simbolos[self.turno]
            self.display.limpiar_pantalla()

            # ¿Ganó el jugador actual?
            if self.hay_ganador(self.simbolos[self.turno]):
                self.display.mostrar_tablero(self.tablero)
                print(f"¡Felicidades {self.turno}! 🎉 Has ganado.\n")
                self.score_manager.guardar_resultado(self.nombre1, self.nombre2, f"Gana {self.turno}")
                input("Presiona Enter para volver al menú...")
                break

            # ¿Empate?
            if self.tablero_lleno():
                self.display.mostrar_tablero(self.tablero)
                print("¡Empate! 🤝\n")
                self.score_manager.guardar_resultado(self.nombre1, self.nombre2, "Empate")
                input("Presiona Enter para volver al menú...")
                break

            # Cambiar de jugador
            self.turno = self.nombre2 if self.turno == self.nombre1 else self.nombre1
