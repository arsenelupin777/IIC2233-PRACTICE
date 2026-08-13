from pathlib import Path

from entities import Item, Usuario

from utils.pretty_print import print_items, print_canasta, print_usuario

def cargar_items() -> list:
    lista_return = []
    path = Path("utils") / "items.dcc"
    with path.open(mode = "r") as archivo:
        lineas = archivo.read().splitlines()
    items = []
    for linea in lineas:
        items.append(linea.split(","))
    for item in items:
        nombre, precio, puntos = item
        lista_return.append(Item(nombre, int(precio), int(puntos)))
    return lista_return

def crear_usuario(tiene_suscripcion: bool) -> Usuario:
    user = Usuario(tiene_suscripcion)
    if tiene_suscripcion:
        print(f"> Usuario con suscripcion. Puntos: {user.puntos}")
    else:
        print(f"> Usuario con suscripcion. Puntos: {user.puntos}")
    return user
if __name__ == "__main__":
    # 1) Crear usuario (con o sin suscripcion)
    usuario_actual = crear_usuario(True)
    # 2) Cargar los items
    items_disponibles = cargar_items()
    # 3) Imprimir todos los items usando los módulos de pretty_print
    print_items(items_disponibles)
    # 4) Agregar todos los items a la canasta del usuario
    for item in items_disponibles:
        usuario_actual.agregar_item(item)
    # 5) Imprimir la canasta del usuario usando los módulos de pretty_print
    print_canasta(usuario_actual)
    # 6) Generar la compra desde el usuario
    usuario_actual.comprar()
    # 7) Imprimir el usuario usando los módulos de pretty_print
    print_usuario(usuario_actual)
