"""Biblioteca de consola: diccionarios y conjuntos de la Unidad 2."""


def datos_ejemplo():
    catalogo = {
        "L003": {"titulo": "Breve historia del tiempo", "autor": "Stephen Hawking"},
        "L001": {"titulo": "Don Quijote de la Mancha", "autor": "Miguel de Cervantes"},
        "L002": {"titulo": "Cien años de soledad", "autor": "Gabriel García Márquez"},
    }
    socios = {"S001", "S002", "S003", "S004"}
    prestamos = {"novela": {"S001", "S002"}, "ciencia": {"S002", "S003"}}
    return catalogo, socios, prestamos


def registrar_libro(catalogo, codigo, titulo, autor):
    # R1: consulta e inserción en dict: O(1) promedio; O(n) peor caso.
    if codigo in catalogo:
        return False
    catalogo[codigo] = {"titulo": titulo, "autor": autor}
    return True


def buscar_libro(catalogo, codigo):
    # R1: acceso por clave: O(1) promedio; O(n) peor caso.
    return catalogo.get(codigo)


def catalogo_ordenado(catalogo):
    # R2: ordenar n códigos: O(n log n); construir la lista: O(n).
    return [(codigo, catalogo[codigo]) for codigo in sorted(catalogo)]


def registrar_socio(socios, identificador):
    # R3: pertenencia e inserción en set: O(1) promedio; O(s) peor caso.
    if identificador in socios:
        return False
    socios.add(identificador)
    return True


def socio_registrado(socios, identificador):
    # R3: pertenencia en set: O(1) promedio; O(s) peor caso.
    return identificador in socios


def registrar_prestamo(socios, prestamos, identificador, genero):
    # Verificación e inserción: O(1) promedio.
    if not socio_registrado(socios, identificador) or genero not in prestamos:
        return False
    prestamos[genero].add(identificador)
    return True


def analizar_prestamos(novela, ciencia):
    # R4: intersección: O(min(a, b)) promedio.
    ambos = novela & ciencia
    # R4: diferencia: O(a) promedio.
    solo_novela = novela - ciencia
    # R4: unión: O(a + b) promedio.
    total = novela | ciencia
    return ambos, solo_novela, total


def pedir_texto(mensaje):
    while True:
        texto = input(mensaje).strip()
        if texto:
            return texto
        print("El valor no puede estar vacío.")


def mostrar_socios(etiqueta, conjunto):
    # Ordenar para presentar k identificadores: O(k log k).
    print(f"{etiqueta}: {', '.join(sorted(conjunto)) or '(ninguno)'}")


def main():
    catalogo, socios, prestamos = datos_ejemplo()
    print("Biblioteca - Unidad 2 (datos en memoria)")
    while True:
        print("\n1. Registrar libro\n2. Buscar libro\n3. Catálogo ordenado"
              "\n4. Registrar socio\n5. Verificar socio\n6. Registrar préstamo por género"
              "\n7. Analizar préstamos\n0. Salir")
        try:
            opcion = input("Opción: ").strip()
            if opcion == "0":
                print("Hasta pronto.")
                break
            if opcion == "1":
                codigo = pedir_texto("Código: ").upper()
                titulo = pedir_texto("Título: ")
                autor = pedir_texto("Autor: ")
                ok = registrar_libro(catalogo, codigo, titulo, autor)
                print("Libro registrado." if ok else "El código ya existe.")
            elif opcion == "2":
                libro = buscar_libro(catalogo, pedir_texto("Código: ").upper())
                print(f"{libro['titulo']} - {libro['autor']}" if libro else "Libro no encontrado.")
            elif opcion == "3":
                if not catalogo:
                    print("Catálogo vacío.")
                for codigo, libro in catalogo_ordenado(catalogo):
                    print(f"{codigo}: {libro['titulo']} - {libro['autor']}")
            elif opcion == "4":
                ok = registrar_socio(socios, pedir_texto("Identificador: ").upper())
                print("Socio registrado." if ok else "El socio ya está registrado.")
            elif opcion == "5":
                ok = socio_registrado(socios, pedir_texto("Identificador: ").upper())
                print("Socio registrado." if ok else "Socio no registrado.")
            elif opcion == "6":
                identificador = pedir_texto("Identificador: ").upper()
                genero = pedir_texto("Género (novela/ciencia): ").lower()
                ok = registrar_prestamo(socios, prestamos, identificador, genero)
                print("Préstamo registrado (sin duplicar socios por género)." if ok
                      else "Socio no registrado o género inválido.")
            elif opcion == "7":
                ambos, solo, total = analizar_prestamos(prestamos['novela'], prestamos['ciencia'])
                mostrar_socios("Ambos géneros", ambos)
                mostrar_socios("Solo novela", solo)
                mostrar_socios("Socios distintos con préstamos", total)
                print(f"Total: {len(total)}")
            else:
                print("Opción inválida.")
        except (EOFError, KeyboardInterrupt):
            print("\nPrograma finalizado.")
            break


if __name__ == "__main__":
    main()
