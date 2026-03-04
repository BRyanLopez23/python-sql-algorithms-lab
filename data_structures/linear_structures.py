"""
Estructuras de Datos Lineales: Lista Enlazada Simple, Pila (LIFO) y Cola (FIFO).
Autor: Bryan Francisco López León (github.com/BRyanLopez23)
"""
from typing import Any, Generic, TypeVar

T = TypeVar("T")


class Nodo(Generic[T]):
    def __init__(self, valor: T) -> None:
        self.valor: T = valor
        self.siguiente: "Nodo[T] | None" = None


class ListaEnlazada(Generic[T]):
    """Implementación POO de Lista Enlazada con inserción O(1) al inicio y recorrido O(n)."""

    def __init__(self) -> None:
        self.cabeza: Nodo[T] | None = None
        self._longitud: int = 0

    def insertar_inicio(self, valor: T) -> None:
        nuevo = Nodo(valor)
        nuevo.siguiente = self.cabeza
        self.cabeza = nuevo
        self._longitud += 1

    def insertar_final(self, valor: T) -> None:
        nuevo = Nodo(valor)
        if not self.cabeza:
            self.cabeza = nuevo
        else:
            actual = self.cabeza
            while actual.siguiente:
                actual = actual.siguiente
            actual.siguiente = nuevo
        self._longitud += 1

    def buscar(self, objetivo: T) -> bool:
        actual = self.cabeza
        while actual:
            if actual.valor == objetivo:
                return True
            actual = actual.siguiente
        return False

    def a_lista(self) -> list[T]:
        resultado: list[T] = []
        actual = self.cabeza
        while actual:
            resultado.append(actual.valor)
            actual = actual.siguiente
        return resultado

    def __len__(self) -> int:
        return self._longitud


class PilaLIFO(Generic[T]):
    """Pila (Stack - Last In, First Out) para evaluación de expresiones y backtracking."""

    def __init__(self) -> None:
        self._items: list[T] = []

    def apilar(self, item: T) -> None:
        self._items.append(item)

    def desapilar(self) -> T:
        if self.esta_vacia():
            raise IndexError("La pila está vacía.")
        return self._items.pop()

    def cima(self) -> T:
        if self.esta_vacia():
            raise IndexError("La pila está vacía.")
        return self._items[-1]

    def esta_vacia(self) -> bool:
        return len(self._items) == 0


def validar_parentesis_balanceados(expresion: str) -> bool:
    """Caso clásico de entrevista técnica utilizando PilaLIFO O(n)."""
    pila = PilaLIFO[str]()
    pares = {")": "(", "]": "[", "}": "{"}
    for char in expresion:
        if char in "([{":
            pila.apilar(char)
        elif char in ")]}":
            if pila.esta_vacia() or pila.desapilar() != pares[char]:
                return False
    return pila.esta_vacia()
