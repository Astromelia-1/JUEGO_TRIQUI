class TriquiPlayers:
    def __init__(self):
        self.nombre1 = ""
        self.nombre2 = ""

    def pedir_nombres(self):
        print("╔══════════════════════╗")
        print("║     JUEGO TRIQUI     ║")
        print("╚══════════════════════╝")
        print("                        ")
        print("== Registro de jugadores ==")
        print("                        ")
        self.nombre1 = self._pedir_nombre("Jugador 1")
        self.nombre2 = self._pedir_nombre("Jugador 2", diferente_a=self.nombre1)
        return self.nombre1, self.nombre2

    def _pedir_nombre(self, etiqueta, diferente_a=None):
        while True:
            nombre = input(f"{etiqueta}, ingresa tu nombre: ").strip()
            if not nombre:
                print("⚠️  El nombre no puede estar vacío.")
                continue
            if diferente_a and nombre == diferente_a:
                print("⚠️  Los nombres de los jugadores no pueden ser iguales.")
                continue
            return nombre

    def mostrar_jugadores(self):
        print(f"Jugador 1: {self.nombre1} (X)")
        print(f"Jugador 2: {self.nombre2} (O)")
