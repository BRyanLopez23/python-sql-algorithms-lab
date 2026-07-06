"""
Suite de Pruebas Unitarias (unittest) para validar estructuras de datos y algoritmos.
Autor: Bryan Francisco López León (github.com/BRyanLopez23)
"""
import unittest
from data_structures.linear_structures import ListaEnlazada, validar_parentesis_balanceados
from data_structures.binary_search_tree import ArbolBinarioBusqueda
from algorithms.sorting_and_searching import quicksort, mergesort, two_sum_hash


class TestAlgorithmsAndStructures(unittest.TestCase):

    def test_lista_enlazada(self) -> None:
        lista = ListaEnlazada[int]()
        lista.insertar_final(10)
        lista.insertar_final(20)
        lista.insertar_inicio(5)
        self.assertEqual(lista.a_lista(), [5, 10, 20])
        self.assertTrue(lista.buscar(10))
        self.assertFalse(lista.buscar(99))

    def test_parentesis_balanceados(self) -> None:
        self.assertTrue(validar_parentesis_balanceados("{[()()]}"))
        self.assertFalse(validar_parentesis_balanceados("{[(])}"))

    def test_bst_inorden(self) -> None:
        bst = ArbolBinarioBusqueda()
        bst.insertar(50, "Raíz")
        bst.insertar(30, "Izq")
        bst.insertar(70, "Der")
        claves = [k for k, _ in bst.recorrido_inorden()]
        self.assertEqual(claves, [30, 50, 70])
        self.assertEqual(bst.buscar(30), "Izq")

    def test_sorting_and_two_sum(self) -> None:
        desordenado = [64, 34, 25, 12, 22, 11, 90]
        esperado = [11, 12, 22, 25, 34, 64, 90]
        self.assertEqual(quicksort(desordenado), esperado)
        self.assertEqual(mergesort(desordenado), esperado)
        self.assertEqual(two_sum_hash([2, 7, 11, 15], 9), (0, 1))


if __name__ == "__main__":
    unittest.main()
