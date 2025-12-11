from Vivienda import vivienda


class casasUni(vivienda):
    def __init__(self, calle, numero, ciudad, superficie, precio_mensual, estado, patio, jardin, adosadas, aparcamiento):
        super().__init__(calle, numero, ciudad, superficie, precio_mensual, estado)
        self.patio = patio
        self.jardin = jardin
        self.adosadas = adosadas
        self.aparcamiento = aparcamiento

    def __str__(self):
        return (
            f"Casa unifamiliar:\n"
            f"  Calle: {self.calle}\n"
            f"  Número: {self.numero}\n"
            f"  Ciudad: {self.ciudad}\n"
            f"  Superficie: {self.superficie} m2\n"
            f"  Precio mensual: {self.precio_mensual} €\n"
            f"  Patio: {'Sí' if self.patio else 'No'}\n"
            f"  Jardín: {'Sí' if self.jardin else 'No'}\n"
            f"  Adosada: {'Sí' if self.adosadas else 'No'}\n"
            f"  Aparcamiento: {'Sí' if self.aparcamiento else 'No'}\n"
            f"  Estado: {'Disponible' if self.estado else 'Ocupada'}\n"
            f"  Inquilino: {self.inquilino.nombre if self.inquilino else 'Sin inquilino'}")