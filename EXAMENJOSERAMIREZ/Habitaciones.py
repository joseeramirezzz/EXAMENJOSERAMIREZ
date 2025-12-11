class habitaciones:
    def __init__(self, tipo, superficie, ventana_ext):
        self.tipo = tipo
        self.superficie = superficie
        self.ventana_ext = ventana_ext

    def __str__(self):
        return (
            f"Habitación:\n"
            f"  Tipo: {self.tipo}\n"
            f"  Superficie: {self.superficie} m2\n"
            f"  Ventana exterior: {'Sí' if self.ventana_ext else 'No'}")