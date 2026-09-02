"""
Lab 1 — Implementación de la clase Pila (Stack)
INF 222 Estructura de Datos · Semestre 2026-2
Estudiante:  Maria Gonsalez 
Grupo: Lab B
Fecha: 2/9/2026
"""


class Pila:
    """
    Implementación de una pila (stack) usando una lista de Python como
    contenedor interno. Principio LIFO: el último elemento insertado es
    el primero en salir.
    """

    def __init__(self):
        """Inicializa una pila vacía."""
        self._datos = []  # el tope de la pila está en el índice -1

    def push(self, dato):
        """
        Agrega `dato` al tope de la pila.
        Complejidad: O(1) amortizado.
        """
        # TODO: implementa este método
        pass

    def pop(self):
        """
        Elimina y retorna el elemento del tope de la pila.
        Lanza IndexError si la pila está vacía.
        Complejidad: O(1) amortizado.
        """
        # TODO: implementa este método
        # Recuerda verificar si la pila está vacía antes de operar
        pass

    def peek(self):
        """
        Retorna (sin eliminar) el elemento del tope de la pila.
        Lanza IndexError si la pila está vacía.
        Complejidad: O(1).
        """
        # TODO: implementa este método
        pass

    def is_empty(self):
        """
        Retorna True si la pila no contiene elementos, False en caso contrario.
        Complejidad: O(1).
        """
        # TODO: implementa este método
        pass

    def size(self):
        """
        Retorna el número de elementos en la pila.
        Complejidad: O(1).
        """
        # TODO: implementa este método
        pass

    def __str__(self):
        """
        Retorna una representación legible de la pila.
        Formato sugerido: Pila (tope -> base): [3, 2, 1]
        Complejidad: O(n).
        """
        # TODO: implementa este método
        pass


# =============================================================================
# CASOS DE PRUEBA
# Agrega aquí al menos 5 casos de prueba. Usa print() para mostrar resultados
# y verifica que cada caso produce la salida esperada.
# =============================================================================

if __name__ == "__main__":
    print("=" * 50)
    print("Pruebas de la clase Pila")
    print("=" * 50)

    # Caso 1: Pila vacía
    # TODO: crea una pila vacía y verifica is_empty()
    pila = Pila()
    print(f"Caso 1 - ¿Pila vacía recién creada?: {pila.is_empty()} (Esperado: True)")
    print(f"Caso 1 - Tamaño inicial: {pila.size()} (Esperado: 0)")
    print("-" * 50)

    # Caso 2: push de 3 elementos
    # TODO: agrega 3 elementos y verifica size()
    pila.push(10)
    pila.push(20)
    pila.push(30)
    print(f"Caso 2 - Estado de la pila tras 3 push: {pila}")
    print(f"Caso 2 - Tamaño actual: {pila.size()} (Esperado: 3)")
    print(f"Caso 2 - ¿Pila vacía?: {pila.is_empty()} (Esperado: False)")
    print("-" * 50)

    # Caso 3: peek sin modificar la pila
    # TODO: verifica que peek retorna el tope y la pila no cambia
    tope = pila.peek()
    print(f"Caso 3 - Elemento en el tope (peek): {tope} (Esperado: 30)")
    print(f"Caso 3 - Tamaño después de peek: {pila.size()} (Esperado: 3)")
    print(f"Caso 3 - Estado de la pila: {pila}")
    print("-" * 50)
    # Caso 4: pop retorna el tope
    # TODO: haz pop y verifica el valor retornado
    eliminado = pila.pop()
    print(f"Caso 4 - Elemento desapilado (pop): {eliminado} (Esperado: 30)")
    print(f"Caso 4 - Nuevo tope tras pop: {pila.peek()} (Esperado: 20)")
    print(f"Caso 4 - Estado actual: {pila}")
    print("-" * 50)
    # Caso 5: pop en pila vacía lanza IndexError
    # TODO: usa try/except para verificar que se lanza IndexError
    pila_vacia = Pila()
    try:
        pila_vacia.pop()
    except IndexError as e:
        print(f"Caso 5 - Excepción capturada correctamente en pop(): {e}")
    print("-" * 50)
    # Caso 6 en adelante: agrega tus propios casos de prueba
    try:
        pila_vacia.peek()
    except IndexError as e:
        print(f"Caso 6 - Excepción capturada correctamente en peek(): {e}")
    print("-" * 50)
    # Caso 7: Vaciar completamente la pila
    print("Caso 7 - Vaciando la pila...")
    pila.pop()  # elimina 20
    pila.pop()  # elimina 10
    print(f"Caso 7 - Tamaño final: {pila.size()} (Esperado: 0)")
    print(f"Caso 7 - ¿Está vacía?: {pila.is_empty()} (Esperado: True)")
    print("=" * 50)