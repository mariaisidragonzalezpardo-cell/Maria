"""
Lab 4 — Referencias y Aliasing en Python
INF 222 Estructura de Datos · Semestre 2026-2
Estudiante: María González
Grupo: Lab, B
Fecha: 16/9/2026

Instrucciones:
    Para cada fragmento de código, PRIMERO escribe tu predicción en el comentario
    "PREDICCIÓN:", LUEGO ejecuta y registra el resultado real en "RESULTADO:".
    Usa Python Tutor para visualizar el estado de la memoria.
"""

import copy

print("=" * 55)
print("PARTE 1 — id() y referencias básicas")
print("=" * 55)

# Experimento 1.1: referencias a enteros
a = 42
b = a
# PREDICCIÓN: ¿son a y b el mismo objeto? (id(a) == id(b) → True/False)
# Tu predicción: True
print(f"1.1 id(a) == id(b): {id(a) == id(b)}")
# RESULTADO: True
# EXPLICACIÓN: b = a , b recibe la misma referencia que a, ambos aputan al mismo objeto entero 42.

# Experimento 1.2: reasignación no afecta al original
a = 42
b = a
b = 99
# PREDICCIÓN: ¿qué valor tiene a después de b = 99?
# Tu predicción: a = 42
print(f"1.2 a = {a}  (b fue reasignado a 99)")
# RESULTADO: 42
# EXPLICACION: Como los enteros son inmutables, la reasignacion de b = 99 no afecta a 42, ya que b ahora apunta a nuevo objetivo 99 en memoria, mientras que a sigue apuntando a 42.

print("\n" + "=" * 55)
print("PARTE 2 — Aliasing con listas")
print("=" * 55)

# Experimento 2.1: aliasing
lista_a = [1, 2, 3]
lista_b = lista_a          # ← esto NO copia la lista
lista_b.append(99)
# PREDICCIÓN: ¿qué contiene lista_a?
# Tu predicción: lista_a = [1, 2, 3, 99]
print(f"2.1 lista_a = {lista_a}  (lista_b.append(99))")
# RESULTADO: [1, 2, 3, 99]
# EXPLICACIÓN: lista_b = lista_a no copia la lista, ambas variable apuntan al mismo objecto. Modificar lista_b altera al objeto compartido, por lo que lista_a tambien refleja el cambio.

# Experimento 2.2: copia superficial (shallow copy)
lista_a = [1, 2, 3]
lista_c = lista_a.copy()   # ← esto SÍ crea una copia nueva
lista_c.append(99)
# PREDICCIÓN: ¿qué contiene lista_a ahora?
# Tu predicción: lista_a = [1, 2, 3]
print(f"2.2 lista_a = {lista_a}  (lista_c.copy() y lista_c.append(99))")
# RESULTADO: [1, 2, 3]
# EXPLICACION: lista_c = lista_a.copy() crea un nuevo objecto lista_c, por lo que modificar lista_c, no altera a la lista_a.

# Experimento 2.3: copia superficial con listas anidadas
original = [[1, 2], [3, 4]]
copia_superficial = original.copy()
copia_superficial[0].append(99)   # modifica la sublista
# PREDICCIÓN: ¿qué contiene original[0]?
# Tu predicción: original[0] = [1, 2, 99]
print(f"2.3 original[0] = {original[0]}  (shallow copy + append interno)")
# RESULTADO: [1, 2, 99]
# EXPLICACIÓN: La copia superficial duplico el contenedor principal, pero las sublista siguen compartiendo la misma referencia. Por lo tanto, modificar la sublista en copia_superficial afecta a original. 

# Experimento 2.4: copia profunda (deep copy)
original = [[1, 2], [3, 4]]
copia_profunda = copy.deepcopy(original)
copia_profunda[0].append(99)
# PREDICCIÓN: ¿qué contiene original[0] ahora?
# Tu predicción: original[0] = [1, 2]
print(f"2.4 original[0] = {original[0]}  (deep copy + append interno)")
# RESULTADO: [1, 2]
# ExPLICACION: copy.deepcopy() duplica recursivamente todos los objectos, por lo que modificar la sublista en copia_profunda no afecta a la original.

print("\n" + "=" * 55)
print("PARTE 3 — Funciones: mutar vs. retornar copia")
print("=" * 55)


def agregar_elemento_in_situ(lista, elemento):
    """Modifica la lista original (mutación in situ)."""
    lista.append(elemento)
    # No retorna nada (retorna None implícitamente)


def agregar_elemento_copia(lista, elemento):
    """
    Retorna una nueva lista con el elemento agregado.
    La lista original NO se modifica.
    """
    # TODO: nueva_lista = lista.copy()
    nueva_lista = lista.copy()
    nueva_lista.append(elemento)
    return nueva_lista


# Prueba de mutar in situ
mi_lista = [1, 2, 3]
agregar_elemento_in_situ(mi_lista, 4)
print(f"3.1 in_situ:  mi_lista = {mi_lista}  (esperado: [1, 2, 3, 4])")

# Prueba de retornar copia
mi_lista = [1, 2, 3]
nueva_lista = agregar_elemento_copia(mi_lista, 4)
print(f"3.2 copia:    mi_lista  = {mi_lista}   (esperado: [1, 2, 3] — sin cambios)")
print(f"             nueva_lista = {nueva_lista}  (esperado: [1, 2, 3, 4])")

print("\n" + "=" * 55)
print("PARTE 4 — Predicciones adicionales (escribe ANTES de ejecutar)")
print("=" * 55)

# Fragmento 4.1
x = [10, 20, 30]
y = x
x = [40, 50]  # reasignación (no mutación)
# PREDICCIÓN: ¿qué contiene y?
# Tu predicción: y = [10, 20, 30]
print(f"4.1 y = {y}")
# RESULTADO: [10, 20, 30]
# EXPLICACION: La variable "y" guarda la referencia de la lista incial [10, 20, 30].
# Reasignar x = [40, 50] hace que x apunte a un nuevo objecto lista, pero no modifica la lista que apunta y.

# Fragmento 4.2
def modificar(lst):
    lst += [99]   # ¿es esto lo mismo que lst.append(99)?

nums = [1, 2, 3]
modificar(nums)
# PREDICCIÓN: ¿qué contiene nums?
# Tu predicción: nums = [1, 2, 3, 99]
print(f"4.2 nums = {nums}")
# RESULTADO: [1, 2, 3, 99]
# EXPLICACION: El operador += es la lista invoca el metodo dinamico __iadd__, el cual realiza una mutacion in situ modificando el objecto original
# Si se hubiera utilizado lst = lst + [99],se habria creado un objeto nuevo sin modificar nums.

# NOTA: += en listas llama a __iadd__ que modifica in situ,
#       mientras que + crea una lista nueva. Investiga la diferencia.
print("\n" + "=" * 55)
print("DECLARACIÓN DEL USO DE INTELIGENCIA ARTIFICIAL")
print("=" * 55)
"""
DECLARACIÓN DE USO DE IA ACADÉMICA:

1. Asistente utilizado: IA Generativa (Gemini).
2. Formas de apoyo recibidas:
   - Explicación conceptual sobre la diferencia entre punteros en C y el modelo de referencias en Python.
   -  Una guía paso a paso para la  implementación de la función.
   - Clarificación conceptual de los operadores de mutación in situ vs reasignación (métodos __iadd__ y copy.deepcopy).
"""