class Te:
    duracion = 365 #duracion en dias

    @staticmethod
    def retorna_tiempo_y_recomendacion(sabor):
        if sabor == 1:
            return (
                3,
                "Al desayunar",
            )
        elif sabor == 2:
            return (
                5,
                "Al medio día",
            )
        elif sabor == 3:
            return (
                6,
                "Al atardecer",
            )
        else:
            return None, "Sabor no válido"

    @staticmethod
    def retorna_precio(formato):
        if formato == 300:
            return 3000
        elif formato == 500:
            return 5000
        else:
            return None
