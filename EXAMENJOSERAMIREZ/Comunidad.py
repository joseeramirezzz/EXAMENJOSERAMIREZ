class comunidad:
    def __init__(self, nombre, direccion_ref, presupuesto_anual):
        self.nombre = nombre
        self.direccion_ref = direccion_ref
        self.presupuesto_anual = presupuesto_anual
        self.viviendas = []

    def agregar_vivienda(self, vivienda):
        self.viviendas.append(vivienda)

    def quitar_vivienda(self, vivienda):
        if vivienda in self.viviendas:
            self.viviendas.remove(vivienda)

    def __str__(self):
        return (
            f"Comunidad:\n"
            f"  Nombre: {self.nombre}\n"
            f"  Dirección: {self.direccion_ref}\n"
            f"  Presupuesto anual: {self.presupuesto_anual} €\n"
            f"  Número de viviendas: {len(self.viviendas)}")