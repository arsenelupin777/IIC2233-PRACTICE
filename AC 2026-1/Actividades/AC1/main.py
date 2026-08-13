from pathlib import Path

from entities import Medallista, TablaPuntajes

from utils.pretty_print import print_medallista, print_puntajes

def cargar_medallistas(path: str) -> list:
    lista = []
    ruta = Path(path)
    with ruta.open(mode = "r",encoding = "utf-8") as doc:
        medallistas = doc.read().splitlines()
    for medallista in medallistas:
        nombre, pais, deporte, medalla = medallista.split(",")
        lista.append(Medallista(nombre, deporte, medalla, pais))
    return lista

def crear_tabla(medallistas: list[Medallista]) -> TablaPuntajes:
    tabla = TablaPuntajes()
    for medallista in medallistas:
        tabla.agregar_medallista(medallista)
    return tabla

if __name__ == "__main__":
    medallistas = cargar_medallistas("utils/results.dcc")
    for medallista in medallistas:
        print_medallista(medallista)
    tabla = crear_tabla(medallistas)
    paises_ordenados = tabla.ordenar_paises()
    print_puntajes(paises_ordenados)
