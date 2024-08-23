class Pelota:
    forma = "redondeada"

    def asigna_color(self, nuevo_color: str):
        self.color = nuevo_color

    def lee_color_y_forma(self):
        print("El color de esta pelota es {}".format(self.color))
        print("La forma de esta pelota es {}".format(self.forma))


print(Pelota.forma)

p = Pelota()
p.asigna_color("rojo")

# Salida: El color de esta pelota es rojo
p.lee_color_y_forma()
