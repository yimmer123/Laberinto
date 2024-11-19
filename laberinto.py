import random

# Definir las dimensiones del laberinto
ANCHO = 20
ALTO = 10

# Generar el laberinto vacío (lleno de paredes)
laberinto = [['#' for _ in range(ANCHO)] for _ in range(ALTO)]

# Función para generar un laberinto simple
def generar_laberinto(x, y):
    # Direcciones para explorar (arriba, derecha, abajo, izquierda)
    direcciones = [(0, -2), (2, 0), (0, 2), (-2, 0)]
    random.shuffle(direcciones)  # Aleatorizar las direcciones

    for dx, dy in direcciones:
        nx, ny = x + dx, y + dy
        if 0 < nx < ALTO - 1 and 0 < ny < ANCHO - 1 and laberinto[nx][ny] == '#':
            # Hacer un camino
            laberinto[nx][ny] = ' '
            laberinto[x + dx // 2][y + dy // 2] = ' '  # Abrir un pasaje entre el nodo actual y el nuevo
            generar_laberinto(nx, ny)  # Recursivamente generar caminos

# Función para guardar el laberinto en un archivo
def guardar_laberinto_en_archivo(nombre_archivo):
    with open(nombre_archivo, 'w') as archivo:
        for fila in laberinto:
            archivo.write(''.join(fila) + '\n')

# Establecer el punto de inicio
inicio_x, inicio_y = 1, 1
laberinto[inicio_x][inicio_y] = 'S'  # S para Start (inicio)

# Establecer el punto de finalización
fin_x, fin_y = ALTO - 2, ANCHO - 2
laberinto[fin_x][fin_y] = 'F'  # F para Finish (fin)

# Generar el laberinto a partir del punto de inicio
generar_laberinto(inicio_x, inicio_y)

# Guardar el laberinto en un archivo .txt
guardar_laberinto_en_archivo('laberinto.txt')

print("Laberinto guardado en 'laberinto.txt'")
