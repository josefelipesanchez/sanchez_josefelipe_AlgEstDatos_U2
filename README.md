# Biblioteca - Algoritmos y Estructuras de Datos, Unidad 2

## Ejecución

Requiere Python 3.8 o posterior; no requiere instalar paquetes.
Desde la carpeta del proyecto:

```console
python main.py
```

El menú permite registrar y buscar libros, listar el catálogo ordenado,
registrar y consultar socios, registrar préstamos por género y analizarlos.
La opción 0 termina el programa. Los cambios se conservan solo durante la sesión.

## Requerimientos

- **R1:** `catalogo` es un diccionario cuya clave es el código y cuyo valor
  es otro diccionario con título y autor. Se rechazan códigos repetidos.
- **R2:** `sorted(catalogo)` muestra los códigos en orden lexicográfico.
  Los ejemplos usan L001, L002 y L003. Un TreeMap mantiene sus claves ordenadas
  mediante un árbol balanceado: recorrerlo entrega ese orden sin ordenar otra vez.
  A cambio, buscar e insertar cuesta O(log n). Un `dict` conserva orden de
  inserción, que no necesariamente coincide con el orden de sus claves.
- **R3:** el conjunto `socios` evita duplicados y permite verificar pertenencia.
- **R4:** dos conjuntos de socios con préstamos de novela y ciencia permiten
  calcular intersección (`&`), diferencia (`-`) y unión (`|`). El conjunto registra
  quién tiene préstamos del género; no cuenta libros ni ejemplares individuales.

Los códigos e identificadores ingresados por consola se convierten a mayúsculas.
No se permiten entradas vacías; un préstamo requiere un socio registrado.

## Complejidades

Sea n la cantidad de libros, s la de socios, a la de lectores de novela y b la
de lectores de ciencia. Se consideran claves de longitud acotada.

| Requisito | Operación principal | Tiempo |
|---|---|---|
| R1 | Registrar / buscar libro | O(1) promedio |
| R2 | Ordenar y listar catálogo | O(n log n) |
| R3 | Registrar / verificar socio | O(1) promedio |
| R4 | Intersección | O(min(a, b)) promedio |
| R4 | Diferencia novela - ciencia | O(a) promedio |
| R4 | Unión | O(a + b) promedio |

Las tablas hash pueden degradarse por colisiones: O(n) para una operación de
diccionario y O(s) para una de socios en el peor caso. Ordenar k socios para
mostrarlos agrega O(k log k); no forma parte del cálculo de los conjuntos.

## Prueba rápida

Con los datos iniciales, la opción 3 muestra L001, L002, L003.
La opción 7 produce ambos géneros: S002; solo novela: S001;
unión: S001, S002, S003; total: 3. S004 está registrado sin préstamos.
Registrar S001 otra vez debe rechazar el duplicado.

Para ejecutar la verificación automática:

```console
python -m unittest -v
```

## Publicación pendiente

Autor: José Felipe Sánchez. Nombre previsto: `sanchez_josefelipe_AlgEstDatos_U2`.
Enlace previsto: https://github.com/josefelipesanchez/sanchez_josefelipe_AlgEstDatos_U2

El repositorio local contiene tres commits. La publicación requiere conectar
GitHub; el enlace del informe es el destino previsto y aún no acredita un
repositorio publicado. Los dos primeros commits usan una identidad provisional
(`Autor pendiente`, `autor@example.invalid`). No es una cuenta real. El tercer
commit usa el nombre del autor y el correo privado estándar de GitHub.
