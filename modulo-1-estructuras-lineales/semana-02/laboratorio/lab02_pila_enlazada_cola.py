"""
Lab 2 — Pila Enlazada, Cola y Simulador de Impresión
INF 222 Estructura de Datos · Semestre 2026-2
Estudiante: Maria Gonzalez
Grupo: Lab B
Fecha: 9/9/2026
"""


# =============================================================================
# PARTE 1: NODO (base para la pila enlazada y la cola)
# =============================================================================

class Nodo:
    """Nodo básico con un dato y una referencia al siguiente nodo."""

    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None  # referencia al próximo nodo


# =============================================================================
# PARTE 2: PILA ENLAZADA
# =============================================================================

class PilaEnlazada:
    """
    Pila implementada con nodos enlazados.
    El tope de la pila es la cabeza de la lista de nodos.
    """

    def __init__(self):
        self._cabeza = None  # nodo del tope (None si la pila está vacía)
        self._tamanio = 0

    def push(self, dato):
        """Inserta dato en el tope. Complejidad: O(1)."""
        # TODO: crea un nuevo Nodo, ponlo como nueva cabeza
        nuevo_nodo = Nodo(dato)
        nuevo_nodo.siguiente = self._cabeza
        self._cabeza = nuevo_nodo
        self._tamanio += 1

    def pop(self):
        """Elimina y retorna el dato del tope. Lanza IndexError si está vacía."""
        # TODO: guarda el dato de la cabeza, avanza la cabeza al siguiente
        if self.is_empty():
            raise IndexError("pop from empty stack (pila vacia)")
        dato = self._cabeza.dato
        self._cabeza = self._cabeza.siguiente
        self._tamanio -= 1
        return dato


    def peek(self):
        """Retorna (sin eliminar) el dato del tope. Lanza IndexError si está vacía."""
        # TODO
        if self.is_empty():
            raise IndexError("peek from empty stack (pila vacía)")
        return self._cabeza.dato

    def is_empty(self):
        """Retorna True si la pila está vacía."""
        return self._cabeza is None

    def size(self):
        """Retorna el número de elementos."""
        return self._tamanio

    def __str__(self):
        """Representación: tope → ... → base"""
        # TODO
        elementos = []
        actual = self._cabeza
        while actual is not None:
            elementos.append(str(actual.dato))
            actual = actual.siguiente
        return " → ".join(elementos) if elementos else "Pila Vacía"


# =============================================================================
# PARTE 3: VERIFICADOR DE PARÉNTESIS BALANCEADOS
# =============================================================================

def parentesis_balanceados(cadena):
    """
    Retorna True si todos los pares de paréntesis, corchetes y llaves
    en `cadena` están correctamente balanceados; False en caso contrario.
    Usa la clase PilaEnlazada.

    Ejemplos:
        parentesis_balanceados("({[]})")  → True
        parentesis_balanceados("([)]")    → False
        parentesis_balanceados("{[")      → False
    """
    # TODO: implementa el algoritmo con una PilaEnlazada
    # Tip: define un diccionario de pares cierre→apertura
    pares = {')': '(', ']': '[', '}': '{'}
    aperturas = set(pares.values())
    pila = PilaEnlazada()

    for caracter in cadena:
        if caracter in aperturas:
            pila.push(caracter)
        elif caracter in pares:
            if pila.is_empty():
                return False  # Cierre sin haber abierto
            
            tope = pila.pop()
            if tope != pares[caracter]:
                return False  # Los delimitadores no coinciden

    return pila.is_empty()  # Debe quedar vacía para estar balanceada


# =============================================================================
# PARTE 4: COLA (QUEUE)
# =============================================================================

class Cola:
    """
    Cola implementada con nodos enlazados.
    - enqueue agrega al final (cola)
    - dequeue saca del frente (cabeza)
    """

    def __init__(self):
        self._frente = None  # nodo del frente (primer en salir)
        self._final = None   # nodo del final (último en entrar)
        self._tamanio = 0

    def enqueue(self, dato):
        """Agrega dato al final de la cola. Complejidad: O(1)."""
        # TODO
        nuevo_nodo = Nodo(dato)
        if self.is_empty():
            self._frente = nuevo_nodo
        else:
            self._final.siguiente = nuevo_nodo
        self._final = nuevo_nodo
        self._tamanio += 1

    def dequeue(self):
        """Elimina y retorna el dato del frente. Lanza IndexError si está vacía."""
        # TODO
        if self.is_empty():
            raise IndexError("dequeue from empty queue (cola vacía)")
        dato = self._frente.dato
        self._frente = self._frente.siguiente
        self._tamanio -= 1
        
        if self.is_empty():
            self._final = None
            
        return dato

    def front(self):
        """Retorna (sin eliminar) el dato del frente. Lanza IndexError si está vacía."""
        # TODO
        if self.is_empty():
            raise IndexError("front from empty queue (cola vacía)")
        return self._frente.dato

    def is_empty(self):
        return self._frente is None

    def size(self):
        return self._tamanio

    def __str__(self):
        """Representación: frente → ... → final"""
        # TODO
        elementos = []
        actual = self._frente
        while actual is not None:
            elementos.append(str(actual.dato))
            actual = actual.siguiente
        return " → ".join(elementos) if elementos else "Cola Vacía"


# =============================================================================
# PARTE 5: SIMULADOR DE COLA DE IMPRESIÓN (mini-proyecto)
# =============================================================================

class TrabajoImpresion:
    """Representa un trabajo en la cola de impresión."""

    def __init__(self, nombre, paginas):
        self.nombre = nombre
        self.paginas = paginas

    def __str__(self):
        return f"'{self.nombre}' ({self.paginas} pág.)"


def simulador_impresion(trabajos):
    """
    Simula una cola de impresión. Recibe una lista de tuplas (nombre, páginas).
    Imprime en orden de llegada (FIFO) el nombre de cada trabajo y cuántas páginas tiene.
    Al final muestra el total de páginas impresas.

    Ejemplo de uso:
        trabajos = [("Tesis cap1", 12), ("Factura", 1), ("Informe", 8)]
        simulador_impresion(trabajos)
    """
    # TODO: encola todos los trabajos, luego deséncola uno por uno mostrando el progreso
    cola_impresion = Cola()
    total_paginas = 0

    # Encolar trabajos
    for nombre, paginas in trabajos:
        trabajo = TrabajoImpresion(nombre, paginas)
        cola_impresion.enqueue(trabajo)
        print(f"Encolado: {trabajo}")

    print("\n--- Iniciando Impresión ---")
    
    # Procesar trabajos en orden FIFO
    i = 1
    while not cola_impresion.is_empty():
        trabajo_actual = cola_impresion.dequeue()
        print(f"Imprimiendo trabajo {i}: {trabajo_actual.nombre} ({trabajo_actual.paginas} pág.)... ¡Completado!")
        total_paginas += trabajo_actual.paginas
        i += 1

    print(f"\nProceso finalizado. Total de páginas impresas: {total_paginas}")

# =============================================================================
# TAREA / TRABAJO AUTÓNOMO: EVALUACIÓN EN NOTACIÓN POSTFIJA (RPN)
# =============================================================================

def evaluar_postfija(expresion: str) -> float:
    """
    Evalúa una expresión matemática en Notación Polaca Inversa (Postfija)
    utilizando la clase PilaEnlazada.
    
    Algoritmo:
    1. Divide la cadena por espacios en tokens.
    2. Recorre cada token:
       - Si es un número (operando), se convierte a float y se apila.
       - Si es un operador (+, -, *, /):
         a. Se desapila el segundo operando (b).
         b. Se desapila el primer operando (a).
         c. Se efectúa la operación correspondiente (a op b).
         d. Se apila el resultado obtenido.
    3. Al finalizar, el resultado total queda como único elemento en el tope.
    """
    pila = PilaEnlazada()
    tokens = expresion.split()

    operadores = {'+', '-', '*', '/'}

    for token in tokens:
        if token in operadores:
            if pila.size() < 2:
                raise ValueError("Expresión postfija inválida: faltan operandos.")
            
            b = pila.pop()  # Segundo operando (sacado primero)
            a = pila.pop()  # Primer operando

            if token == '+':
                resultado = a + b
            elif token == '-':
                resultado = a - b
            elif token == '*':
                resultado = a * b
            elif token == '/':
                if b == 0:
                    raise ZeroDivisionError("División por cero en la expresión.")
                resultado = a / b
            
            pila.push(resultado)
        else:
            try:
                numero = float(token)
                pila.push(numero)
            except ValueError:
                raise ValueError(f"Token no válido: {token}")

    if pila.size() != 1:
        raise ValueError("Expresión postfija inválida: sobran operandos.")

    return pila.pop()


# =============================================================================
# CASOS DE PRUEBA
# =============================================================================

if __name__ == "__main__":
    print("=" * 55)
    print("PARTE 2: Pila Enlazada")
    print("=" * 55)
    # TODO: prueba push, pop, peek, is_empty, size, __str__
    pila = PilaEnlazada()
    print("¿Está vacía?:", pila.is_empty())
    
    pila.push(10)
    pila.push(20)
    pila.push(30)
    print("Estado de la pila (tope → base):", pila)
    print("Tamaño:", pila.size())
    print("Tope (peek):", pila.peek())
    
    print("Elemento retirado (pop):", pila.pop())
    print("Estado actual:", pila)

    print("\n" + "=" * 55)
    print("PARTE 3: Verificador de Paréntesis Balanceados")
    print("=" * 55)
    casos = [
        ("({[]})", True),
        ("([)]", False),
        ("{[", False),
        ("", True),          # cadena vacía: balanceada por vacío
        ("3 + (4 * [2])", True),
    ]
    for cadena, esperado in casos:
        resultado = parentesis_balanceados(cadena)
        estado = "OK" if resultado == esperado else "ERROR"
        print(f"  [{estado}] '{cadena}' → {resultado} (esperado: {esperado})")

    print("\n" + "=" * 55)
    print("PARTE 4: Cola")
    print("=" * 55)
    # TODO: prueba enqueue, dequeue, front, is_empty, size
    cola = Cola()
    print("¿Está vacía?:", cola.is_empty())
    
    cola.enqueue("A")
    cola.enqueue("B")
    cola.enqueue("C")
    print("Estado de la cola (frente → final):", cola)
    print("Tamaño:", cola.size())
    print("Frente (front):", cola.front())
    
    print("Elemento retirado (dequeue):", cola.dequeue())
    print("Estado actual:", cola)

    print("\n" + "=" * 55)
    print("PARTE 5: Simulador de Impresión")
    print("=" * 55)
    trabajos = [("Tesis cap1", 12), ("Factura", 1), ("Informe anual", 8), ("CV", 2)]
    simulador_impresion(trabajos)
    print("\n" + "=" * 55)
    print("TRABAJO AUTÓNOMO: Evaluación Postfija")
    print("=" * 55)
    expresiones = [
        ("3 4 + 5 *", 35.0),
        ("5 1 2 + 4 * + 3 -", 14.0),
        ("4 2 /", 2.0)
    ]
    for expr, esperado in expresiones:
        res = evaluar_postfija(expr)
        estado = "OK" if res == esperado else "ERROR"
        print(f"  [{estado}] '{expr}' = {res} (esperado: {esperado})")
