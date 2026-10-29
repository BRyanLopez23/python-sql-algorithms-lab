# 🧠 Python & SQL Data Structures + Algorithms Lab

Repositorio de referencia técnica con implementaciones limpias y documentadas de **Estructuras de Datos**, **Algoritmos Clásicos**, **Programación Orientada a Objetos (POO)**, **Pruebas Unitarias (`unittest`)** y **Consultas SQL Analíticas**.

Desarrollado por **Bryan Francisco López León** ([github.com/BRyanLopez23](https://github.com/BRyanLopez23)) — Software Engineering Student.

---

## 📚 Contenido del Laboratorio

### 1. Estructuras de Datos (`data_structures/`)
* **Listas Enlazadas Genéricas (`ListaEnlazada[T]`):** Inserción `O(1)`, recorrido `O(n)` y búsqueda.
* **Pilas (`PilaLIFO[T]`):** Resolución algorítmica de validación de expresiones y paréntesis balanceados `O(n)`.
* **Árbol Binario de Búsqueda (`ArbolBinarioBusqueda`):** Inserción, búsqueda `O(log n)` y recorrido *In-Order*.

### 2. Algoritmos de Ordenamiento y Búsqueda (`algorithms/`)
* **QuickSort & MergeSort:** Ordenamiento eficiente `O(n log n)`.
* **Two Sum con Tabla Hash:** Optimización de `O(n²)` a `O(n)` en tiempo de ejecución.

### 3. Consultas SQL Avanzadas (`sql_challenges/`)
* Reportes financieros con `INNER JOIN`, `GROUP BY` y `HAVING`.
* Funciones de ventana (`RANK() OVER (PARTITION BY ...)`).
* Expresiones de tabla comunes (`WITH CTE`) para análisis de inventario sin rotación.

---

## 🧪 Ejecutar las Pruebas Unitarias

```bash
python -m unittest discover -s tests
```
