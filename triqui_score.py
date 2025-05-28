import os
import csv
from datetime import datetime

class TriquiScore:
    HISTORIAL_FILE = "historial_triqui.csv"

    def guardar_resultado(self, nombre1: str, nombre2: str, resultado: str) -> None:
        existe = os.path.isfile(self.HISTORIAL_FILE)
        with open(self.HISTORIAL_FILE, "a", newline="", encoding="utf-8") as f:
            writer = csv.writer(f)
            if not existe:
                writer.writerow(["Fecha y hora", "Jugador 1", "Jugador 2", "Resultado"])
            writer.writerow(
                [datetime.now().strftime("%Y-%m-%d %H:%M:%S"), nombre1, nombre2, resultado]
            )

    def mostrar_historial(self) -> None:
        if not os.path.isfile(self.HISTORIAL_FILE):
            print("No hay partidas registradas aún.")
            input("Presiona Enter para volver al menú...")
            return
        print("\n--- HISTORIAL DE PARTIDAS ---")
        with open(self.HISTORIAL_FILE, "r", encoding="utf-8") as f:
            reader = csv.reader(f)
            for row in reader:
                print(" | ".join(row))
        print()
        input("Presiona Enter para volver al menú...")



