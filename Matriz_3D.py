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
    # Puedes agregar más ciudades aquí
]

# Calcular el promedio de temperaturas para cada ciudad y semana
for ciudad_idx, ciudad in enumerate(temperaturas):
    for semana_idx, semana in enumerate(ciudad):
        promedio_semana = sum(semana) / len(semana)
        print(f"Semana {semana_idx + 1}: {promedio_semana}°C")
