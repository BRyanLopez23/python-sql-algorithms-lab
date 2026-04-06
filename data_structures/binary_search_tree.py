"""
Árbol Binario de Búsqueda (BST) y Recorridos (In-Order, Pre-Order, Post-Order).
Autor: Bryan Francisco López León (github.com/BRyanLopez23)
"""
from dataclasses import dataclass
from typing import Optional


@dataclass
class NodoBST:
    clave: int
    valor: str
    izquierdo: Optional["NodoBST"] = None
    derecho: Optional["NodoBST"] = None


class ArbolBinarioBusqueda:
    """Árbol Binario de Búsqueda con inserción y búsqueda O(log n) promedio."""

    def __init__(self) -> None:
        self.raiz: Optional[NodoBST] = None

    def insertar(self, clave: int, valor: str) -> None:
        self.raiz = self._insertar_rec(self.raiz, clave, valor)

    def _insertar_rec(self, nodo: Optional[NodoBST], clave: int, valor: str) -> NodoBST:
        if nodo is None:
            return NodoBST(clave, valor)
        if clave < nodo.clave:
            nodo.izquierdo = self._insertar_rec(nodo.izquierdo, clave, valor)
        elif clave > nodo.clave:
            nodo.derecho = self._insertar_rec(nodo.derecho, clave, valor)
        else:
            nodo.valor = valor
        return nodo

    def buscar(self, clave: int) -> Optional[str]:
        actual = self.raiz
        while actual is not None:
            if clave == actual.clave:
                return actual.valor
            actual = actual.izquierdo if clave < actual.clave else actual.derecho
        return None

    def recorrido_inorden(self) -> list[tuple[int, str]]:
        resultado: list[tuple[int, str]] = []
        self._inorden_rec(self.raiz, resultado)
        return resultado

    def _inorden_rec(self, nodo: Optional[NodoBST], acc: list[tuple[int, str]]) -> None:
        if nodo:
            self._inorden_rec(nodo.izquierdo, acc)
            acc.append((nodo.clave, nodo.valor))
            self._inorden_rec(nodo.derecho, acc)
