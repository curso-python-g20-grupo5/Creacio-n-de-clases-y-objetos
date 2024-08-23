from te import Te

# Crear dos instancias
te_1 = Te()
te_2 = Te()

# Almacenar el tipo de dato
tipo_1 = type(te_1)
tipo_2 = type(te_2)

# Mostrar el tipo de dato
print(tipo_1)
print(tipo_2)

# Comparar si ambos tipos son iguales
if tipo_1 == tipo_2:
    print("Ambos objetos son del mismo tipo")
else:
    print("Los objetos no son del mismo tipo")
