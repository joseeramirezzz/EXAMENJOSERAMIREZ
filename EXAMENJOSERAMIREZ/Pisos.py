from Vivienda import vivienda

class pisos(vivienda):
    def __init__(self, calle, numero, ciudad, superficie, precio_mensual, estado, planta, num_puerta, garaje, trastero):
        super().__init__(calle, numero, ciudad, superficie, precio_mensual, estado)
        self.planta = planta
        self.num_puerta = num_puerta
        self.garaje = garaje
        self.trastero = trastero

    def __str__(self):
        return (
            f"Piso:\n"
            f"  Calle: {self.calle}\n"
            f"  Número: {self.numero}\n"
            f"  Ciudad: {self.ciudad}\n"
            f"  Planta: {self.planta}\n"
            f"  Puerta: {self.num_puerta}\n"
            f"  Superficie: {self.superficie} m2\n"
            f"  Precio mensual: {self.precio_mensual} €\n"
            f"  Garaje: {'Sí' if self.garaje else 'No'}\n"
            f"  Trastero: {'Sí' if self.trastero else 'No'}\n"
            f"  Estado: {'Disponible' if self.estado else 'Ocupada'}\n"
            f"  Inquilino: {self.inquilino.nombre if self.inquilino else 'Sin inquilino'}")
