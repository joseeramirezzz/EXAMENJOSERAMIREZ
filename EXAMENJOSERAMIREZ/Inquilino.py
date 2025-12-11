class inquilino:
    def __init__(self, nombre, DNI, Telefono):
        self.nombre = nombre
        self.DNI = DNI
        self.Telefono = Telefono
        self.vivienda = None

    def cambiar_vivienda(self, nueva_vivienda):
        self.vivienda = nueva_vivienda

    def __str__(self):
        return (
            f"Inquilino:\n"
            f"  Nombre: {self.nombre}\n"
            f"  DNI: {self.DNI}\n"
            f"  Teléfono: {self.Telefono}\n"
            f"  Vivienda asignada: "
            f"{self.vivienda.calle if self.vivienda else 'Ninguna'}")