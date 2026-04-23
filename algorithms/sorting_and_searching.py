"""
Algoritmos de Ordenamiento y Búsqueda (QuickSort, MergeSort, Binary Search, Two Pointers).
Autor: Bryan Francisco López León (github.com/BRyanLopez23)
"""


def quicksort(arr: list[int]) -> list[int]:
    """Ordenamiento rápido QuickSort con complejidad promedio O(n log n)."""
    if len(arr) <= 1:
        return arr
    pivote = arr[len(arr) // 2]
    menores = [x for x in arr if x < pivote]
    iguales = [x for x in arr if x == pivote]
    mayores = [x for x in arr if x > pivote]
    return quicksort(menores) + iguales + quicksort(mayores)


def mergesort(arr: list[int]) -> list[int]:
    """Ordenamiento por mezcla MergeSort estable con complejidad garantizada O(n log n)."""
    if len(arr) <= 1:
        return arr
    medio = len(arr) // 2
    izq = mergesort(arr[:medio])
    der = mergesort(arr[medio:])
    return _merge(izq, der)


def _merge(izq: list[int], der: list[int]) -> list[int]:
    resultado: list[int] = []
    i = j = 0
    while i < len(izq) and j < len(der):
        if izq[i] <= der[j]:
            resultado.append(izq[i])
            i += 1
        else:
            resultado.append(der[j])
            j += 1
    resultado.extend(izq[i:])
    resultado.extend(der[j:])
    return resultado


def two_sum_hash(nums: list[int], objetivo: int) -> tuple[int, int] | None:
    """
    Resolución O(n) del problema clásico Two Sum utilizando Tabla Hash (diccionario).
    Retorna los índices de los dos números que suman 'objetivo'.
    """
    vistos: dict[int, int] = {}
    for idx, num in enumerate(nums):
        complemento = objetivo - num
        if complemento in vistos:
            return (vistos[complemento], idx)
        vistos[num] = idx
    return None
