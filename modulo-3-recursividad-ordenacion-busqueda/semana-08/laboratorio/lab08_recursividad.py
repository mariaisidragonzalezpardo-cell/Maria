"""
Lab 8 — Recursividad (con uso declarado de IA)
INF 222 Estructura de Datos · Semestre 2026-2
Estudiante: María González
Grupo: Lab, B
Fecha: 10/7/2026s

=============================================================
DECLARACIÓN DE USO DE IA 
=============================================================
Herramienta usada      : Claude, Copilot)
Para qué se usó        : Obtuve el trazado de fibonacci(5)
Qué hice yo            : Implementé las funciones; reescribí el trazado con mis palabras
=============================================================
"""

import time
from functools import lru_cache


# =============================================================================
# PARTE 1 — FACTORIAL
# =============================================================================

def factorial(n):
    """
    Calcula n! de forma recursiva.
    Caso base: factorial(0) = 1
    Caso recursivo: factorial(n) = n × factorial(n-1)
    Complejidad: O(n) tiempo, O(n) espacio (por la pila de llamadas).
    """
    if n <= 0:
        return 1
    return n * factorial(n - 1)


# =============================================================================
# PARTE 2 — FIBONACCI
# =============================================================================

def fibonacci_recursivo(n):
    """
    Calcula el n-ésimo número de Fibonacci recursivamente.
    ⚠️  Esta implementación es ineficiente: O(2^n) llamadas.
    Solo para propósitos de análisis y trazado.
    """
    if n <= 0:
        return 0
    if n == 1:
        return 1
    return fibonacci_recursivo(n - 1) + fibonacci_recursivo(n - 2)

@lru_cache(maxsize=None)
def fibonacci_memoizado(n):
    """
    Calcula el n-ésimo número de Fibonacci con memoización.
    O(n) tiempo, O(n) espacio.
    """
    if n <= 0:
        return 0
    if n == 1:
        return 1
    return fibonacci_memoizado(n - 1) + fibonacci_memoizado(n - 2)


def fibonacci_iterativo(n):
    """
    Calcula el n-ésimo número de Fibonacci iterativamente.
    O(n) tiempo, O(1) espacio.
    """
    if n <= 0:
        return 0
    if n == 1:
        return 1
    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, a + b
    return b

# =============================================================================
# PARTE 3 — TORRES DE HANOI
# =============================================================================

movimientos = []  # lista global para registrar los movimientos

def torres_de_hanoi(n, origen, destino, auxiliar):
    """
    Resuelve el problema de Torres de Hanoi para n discos.
    Parámetros:
        n:         número de discos a mover
        origen:    poste donde están los n discos al inicio
        destino:   poste al que deben llegar todos los discos
        auxiliar:  poste auxiliar
    Efecto: agrega strings a `movimientos` con cada movimiento.
    Complejidad: O(2^n - 1) movimientos.
    """
    if n == 1:
        movimientos.append(f"Mover disco 1 de {origen} a {destino}")
        return
    
    #   1. Mover n-1 discos de origen a auxiliar (usando destino como aux)
    torres_de_hanoi(n - 1, origen, auxiliar, destino)
    #   2. Mover el disco n (el más grande) de origen a destino
    movimientos.append(f"Mover disco {n} de {origen} a {destino}")
    #   3. Mover n-1 discos de auxiliar a destino (usando origen como aux)
    torres_de_hanoi(n - 1, auxiliar, destino, origen)


# =============================================================================
# PARTE 4 — TRAZADO CON IA (obligatorio)
# =============================================================================
"""
INSTRUCCIONES:
1. Ejecuta fibonacci_recursivo(5) en tu mente o en papel primero.
2. Luego consulta un asistente de IA con este prompt:
   "Muéstrame el trazado paso a paso de la pila de llamadas de fibonacci(5)
    usando la versión recursiva simple (sin memoización). Usa indentación para
    mostrar la jerarquía de llamadas."
3. Copia el trazado que generó la IA en el espacio de abajo.
4. Reescríbelo CON TUS PROPIAS PALABRAS en el espacio "Trazado propio".
   Dibuja también el diagrama ASCII de la pila de llamadas.

TRAZADO GENERADO POR IA:
fibonacci(5)
├── fibonacci(4)
│   ├── fibonacci(3)
│   │   ├── fibonacci(2)
│   │   │   ├── fibonacci(1) -> 1
│   │   │   └── fibonacci(0) -> 0
│   │   │   Result: 1
│   │   └── fibonacci(1) -> 1
│   │   Result: 2
│   └── fibonacci(2)
│       ├── fibonacci(1) -> 1
│       └── fibonacci(0) -> 0
│       Result: 1
│   Result: 3
└── fibonacci(3)
    ├── fibonacci(2)
    │   ├── fibonacci(1) -> 1
    │   └── fibonacci(0) -> 0
    │   Result: 1
    └── fibonacci(1) -> 1
    Result: 2
Result Final: 5


TRAZADO PROPIO (reescrito por el estudiante, sin copiar de la IA):
Para calcular fibonacci(5), el pogrma necesita sumar a fib(4) + fib(3).
- Primero hay que evaluar la rama izquierda completa, llamada fib(4).
- Para resolver fib(4), llama a fib(3) y luego a fib(2).
- Para fib(3), evalua fib(2) (que retorna a 1 tras sumar base cases fib(1)=1 y fib(0)=0) y le suma fib(1)=1. Obtine 2.
- Una vez resuelto fib(3)=2, calcula fib(2) nuevamente por la derecha de fib(4), lo cual vuelve a hacer el calculo completo dando 1.
- Suma fib(3) [2] + fib(2) [1] pra obtener fib(4) = 3.
- Luego baja a evaluar la rama derecha de llamada original: fib(3). Donde se repite todo el calculo de fib(3) hasta obtener 2.
- Finalmente, fib(5) = fib(4) [3] + fib(3) [2] = 5.
Tambien en fib(3) se calcula dos veces comppleta y fib(2) tres veces, mostrando la eficencia 0(2^n).  


DIAGRAMA ASCII DE LA PILA DE LLAMADAS (dibujado por ti):
[ Pila de Ejecución - Momento de máxima profundidad ]
  |----------------------------------|
  | fibonacci(1) -> Retorna 1        | <-- Pila tope (Caso base)
  | fibonacci(2) -> Espera fib(0)    |
  | fibonacci(3) -> Espera fib(2)    |
  | fibonacci(4) -> Espera fib(3)    |
  | fibonacci(5) -> Espera fib(4)    |
  |----------------------------------|
"""


# =============================================================================
# CASOS DE PRUEBA Y COMPARACIÓN DE TIEMPOS
# =============================================================================

if __name__ == "__main__":
    print("=" * 55)
    print("PARTE 1 — Factorial")
    print("=" * 55)
    for n in [0, 1, 5, 10]:
        print(f"  factorial({n}) = {factorial(n)}")

    print("\n" + "=" * 55)
    print("PARTE 2 — Fibonacci: comparación de eficiencia")
    print("=" * 55)
    casos = [10, 20, 30, 35]
    for n in casos:
        t0 = time.perf_counter()
        r = fibonacci_recursivo(n)
        t_rec = time.perf_counter() - t0

        t0 = time.perf_counter()
        m = fibonacci_memoizado(n)
        t_mem = time.perf_counter() - t0

        t0 = time.perf_counter()
        i = fibonacci_iterativo(n)
        t_it = time.perf_counter() - t0

        assert r == m == i, f"Discrepancia en fib({n}): {r}, {m}, {i}"
        print(f"  fib({n:2d}) = {r:10d} | recursivo: {t_rec:.4f}s | memo: {t_mem:.6f}s | iter: {t_it:.6f}s")

    print("\n" + "=" * 55)
    print("PARTE 3 — Torres de Hanoi (n=3)")
    print("=" * 55)
    movimientos.clear()
    torres_de_hanoi(3, "A", "C", "B")
    print(f"  Total de movimientos para n=3: {len(movimientos)} (esperado: 7)")
    for mov in movimientos:
        print(f"  {mov}")

    print(f"\n  Para n=10: {2**10 - 1} movimientos (2^10 - 1)")
    print(f"  Para n=20: {2**20 - 1:,} movimientos — ¿ves por qué O(2^n) escala mal?")
