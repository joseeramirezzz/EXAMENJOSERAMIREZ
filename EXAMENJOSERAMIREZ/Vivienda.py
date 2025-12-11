class vivienda:
    def __init__(self, calle, numero, ciudad, superficie, precio_mensual, estado):
        self.calle = calle
        self.numero = numero
        self.ciudad = ciudad
        self.superficie = superficie
        self.precio_mensual = precio_mensual
        self.estado = estado
        self.habitaciones = []  
        self.inquilino = None

    def saber_estado(self):
        return "Vivienda disponible" if self.estado else "Vivienda ocupada"

    def __str__(self):
        return (
            f"Vivienda:\n"
            f"  Calle: {self.calle}\n"
            f"  Número: {self.numero}\n"
            f"  Ciudad: {self.ciudad}\n"
            f"  Superficie: {self.superficie} m2\n"
            f"  Precio mensual: {self.precio_mensual} €\n"
            f"  Estado: {'Disponible' if self.estado else 'Ocupada'}\n"
            f"  Inquilino: {self.inquilino.nombre if self.inquilino else 'Sin inquilino'}\n"
            f"  Habitaciones: {self.habitaciones}")

