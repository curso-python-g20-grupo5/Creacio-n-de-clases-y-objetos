class Te:
    #Atributo de Clase
    duracion = 365 #duracion en dias (1 año)

    #Método estático para obtener el tiempo de preparación y la recomendación según el sabor ingresado por parámetro
    @staticmethod
    def retorna_tiempo_y_recomendacion(sabor):
        #Parámetro sabor como un número entero
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

    #Método estático para obtener el precio según el formato ingresado por parámetro (número entero). Debe retornar el precio adecuado
    @staticmethod
    def retorna_precio(formato):
        if formato == 300:
            return 3000
        elif formato == 500:
            return 5000
        else:
            return None
