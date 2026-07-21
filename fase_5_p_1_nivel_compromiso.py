def cabecera_tabla():
    """Imprime la cabecera de la tabla del informe de compromiso de clientes.

    Genera el título, las líneas separadoras y los encabezados de columna:
    ID | Cliente | Clasificación

    No toma argumentos ni retorna valores.
    """
    print("\n")
    print("="*58)
    print("{:^60}".format("***INFORME DE COMPROMISO DE CLIENTES***"))
    print("="* 58)

    headers = ["ID", "Cliente", "Clasificación"]

    for header in headers:
        print("|", end="") 
        print(f"{header:^18}", end="")
    print("|")

    separacion_filas(len(headers))

def separacion_filas(columns):
    """Imprime una línea de separación en la tabla.

    Args:
        columns (int): Número de columnas para generar los separadores.
    """
    for i in range(columns):
        print("|", end="")
        print("–"*18, end="")
    print("|")

def info_fila(id_cliente, info):
    """Imprime una fila de la tabla con la información del cliente.
    
    Args:
        id_cliente (str): Identificación del cliente.
        info (dict): Diccionario con la información del cliente, que debe incluir
            las claves "nombre" y "clasificacion".
    """
    print("|", end="")
    print(f"{id_cliente:^18}", end="")
    print("|", end="")
    print(f"{info["nombre"]:^18}", end="")
    print("|", end="")
    print(f"{info["clasificacion"]:^18}", end="")
    print("|")
    separacion_filas(3)

def generar_reporte(clientes=None):
    """Genera un informe de compromiso de clientes.
    
    Args:
        clientes (dict, optional): Diccionario con la información de los clientes.
        Cada clave es la identificación del cliente y cada valor es un diccionario
    """
    if clientes is not None:
        cabecera_tabla()
        for identificacion, datos in clientes.items():
            info_fila(identificacion, datos)
    else:
        print("No hay clientes para generar el informe.")

def clasificacion_compromiso(duracion, eventos):
    """Clasifica el nivel de compromiso de un cliente según la duración de sesión y eventos realizados.
    
    Args:
        duracion (int): Duración de la sesión del cliente en segundos
        eventos (int): Número de eventos ejecutados por el cliente durante la sesión.

    Returns:
        str: Nivel de compromiso del cliente ("Alto", "Medio" o "Bajo").
            - "Alto": duracion > 180 s y eventos > 8
            - "Bajo": duracion < 60 s o eventos < 3
            - "Medio": todos los demás casos.
    """
    if duracion > 180 and eventos > 8:
        return "Alto"
    if duracion < 60 or eventos < 3:
        return "Bajo"
    return "Medio"

def normalizar_cliente(info):
    """Normaliza una colección de clientes añadiendo la clasificación a cada uno.

    Args:
        info (dict[str, dict]): Diccionario con clientes; cada cliente debe tener
            las claves "duracion" (int) y "eventos" (int).

    Returns:
        dict[str, dict]: Copia del diccionario original donde a cada entrada se ha añadido la clave "clasificacion" con el valor calculado por
        clasificacion_compromiso. Las entradas originales no se modifican.
    """
    info_clientes = {}
    for id_cliente, info_cliente in info.items():
        id_normalizado = {
            "nombre": info_cliente["nombre"],
            "duracion": info_cliente["duracion"],
            "eventos": info_cliente["eventos"]
        }
        duracion = info_cliente["duracion"]
        eventos = info_cliente["eventos"]
        id_normalizado["clasificacion"] = clasificacion_compromiso(duracion, eventos)
        info_clientes[id_cliente] = id_normalizado
    return info_clientes

# Datos de ejemplo para probar la función

clientes = {"A01": {"nombre": "Juan Perez",
                "duracion": 100,
                "eventos": 80},
            "A02": {"nombre": "María García",
                "duracion": 150,
                "eventos": 44},
            "A03": {"nombre": "Carlos López",
                "duracion": 200,
                "eventos": 3},
            "A04": {"nombre": "Ana Martínez",
                "duracion": 10,
                "eventos": 55},
            "A05": {"nombre": "Luis Fernández",
                "duracion": 132,
                "eventos": 77}}

# Normalización de clientes y generación del informe

clientes_normalizados = normalizar_cliente(clientes)
generar_reporte(clientes_normalizados)
