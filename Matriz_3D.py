# Matriz 3D de temperaturas
temperaturas = [
    [  # Ciudad 1
        [25, 26, 24, 23, 22],  # Semana 1
        [27, 28, 26, 24, 23],  # Semana 2
        [24, 23, 25, 26, 27]   # Semana 3
    ],
    [  # Ciudad 2
        [22, 23, 21, 20, 19],  # Semana 1
        [24, 25, 23, 22, 21],  # Semana 2
        [20, 21, 23, 24, 25]   # Semana 3
    ],
]

# Calcular el promedio de temperaturas para cada ciudad y semana
for ciudad_idx, ciudad in enumerate(temperaturas):
    for semana_idx, semana in enumerate(ciudad):
        promedio_semana = sum(semana) / len(semana)
        print(f"Semana {semana_idx + 1}: {promedio_semana}°C")
def calcular_temperatura_promedio_ciudades(temperaturas):
    # Creamos una lista para almacenar los promedios de temperatura de cada ciudad
    promedios_ciudades = []

    # Iteramos sobre cada ciudad en la lista de temperaturas
    for ciudad in temperaturas:
        # Creamos una lista para almacenar los promedios de temperatura de cada semana de la ciudad
        promedios_semanales = []

        # Iteramos sobre cada semana de la ciudad
        for semana in ciudad:
            # Calculamos el promedio de temperatura para esta semana
            promedio_semana = sum(semana) / len(semana)
            # Agregamos el promedio de la semana a la lista de promedios semanales
            promedios_semanales.append(promedio_semana)

        # Calculamos el promedio de temperatura para la ciudad sumando los promedios de las semanas y dividiendo por el número de semanas
        promedio_ciudad = sum(promedios_semanales) / len(promedios_semanales)
        # Agregamos el promedio de la ciudad a la lista de promedios de ciudades
        promedios_ciudades.append(promedio_ciudad)

    return promedios_ciudades

# Ejemplo de datos
temperaturas = [
    [  # Ciudad 1
        [25, 26, 24, 23, 22],  # Semana 1
        [27, 28, 26, 24, 23],  # Semana 2
        [24, 23, 25, 26, 27]   # Semana 3
    ],
    [  # Ciudad 2
        [22, 23, 21, 20, 19],  # Semana 1
        [24, 25, 23, 22, 21],  # Semana 2
        [20, 21, 23, 24, 25]   # Semana 3
    ]

]

# Llamamos a la función para calcular los promedios de temperatura de cada ciudad
promedios_ciudades = calcular_temperatura_promedio_ciudades(temperaturas)

# Mostramos los promedios de temperatura de cada ciudad
for i, promedio in enumerate(promedios_ciudades):
    print(f"Promedio de temperatura para la Ciudad {i + 1}: {promedio}°C")
