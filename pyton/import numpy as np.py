import numpy as np
from itertools import combinations

def resolver_acertijo_esfinge(preguntas, respuestas):
    """
    Resuelve el acertijo de la Esfinge: 5 ecuaciones con 3 incógnitas (x, y, z), 
    donde exactamente una de las 5 respuestas es una mentira.
    
    Args:
        preguntas (list of list): Lista de 5 filas, cada una [a, b, c] 
                                  de la ecuación ax + by + cz = R.
        respuestas (list): Lista de 5 respuestas R.
        
    Returns:
        tuple: (x, y, z) de las patas verdaderas, o None si no se puede resolver.
    """
    
    # Hay 5 respuestas, por lo que hay 5 combinaciones posibles donde 4 son verdad.
    indices_verdaderos = list(combinations(range(5), 4))
    
    # x, y, z (Axex, Basiliso, Centauro)
    solucion_unica = None

    print(f"Número total de combinaciones a verificar (omitiendo una mentira): {len(indices_verdaderos)}\n")

    for i, indices in enumerate(indices_verdaderos):
        # Tomamos 4 de las 5 ecuaciones para resolver el sistema sobredeterminado.
        # El sistema se resuelve si se usan 3 ecuaciones linealmente independientes.
        
        # Escoger las 4 ecuaciones y respuestas que se ASUME son VERDAD
        A_4x3 = np.array([preguntas[j] for j in indices])
        R_4x1 = np.array([respuestas[j] for j in indices])
        
        # Necesitamos elegir 3 ecuaciones de estas 4 para resolver el sistema 3x3.
        # Iteramos sobre todas las combinaciones de 3 que podemos formar.
        
        print(f"--- Combinación {i+1}: Asumiendo que la respuesta {set(range(5)) - set(indices)} es la Mentira ---")
        
        # Obtenemos las 4 combinaciones de 3 índices para resolver (solo necesitamos 3)
        indices_3x3 = list(combinations(indices, 3))
        
        # Almacenará la solución obtenida de las sub-matrices 3x3
        soluciones_temp = []

        for k, sub_indices in enumerate(indices_3x3):
            A_3x3 = np.array([preguntas[j] for j in sub_indices])
            R_3x1 = np.array([respuestas[j] for j in sub_indices])
            
            # Verificar si la matriz es singular (determinante cero)
            if np.linalg.det(A_3x3) == 0:
                # print(f"    Sub-sistema {k+1}: Matriz singular. No se puede resolver.")
                continue

            try:
                # Resolver el sistema A_3x3 * [x, y, z] = R_3x1
                X = np.linalg.solve(A_3x3, R_3x1)
                
                # Las patas deben ser números enteros no negativos.
                if all(val.is_integer() and val >= 0 for val in X):
                    soluciones_temp.append(tuple(map(int, X)))
                
            except np.linalg.LinAlgError:
                # print(f"    Sub-sistema {k+1}: Error de álgebra lineal (p.ej., singularidad)")
                continue

        # Post-procesamiento: ¿Las soluciones 3x3 encontradas son consistentes?
        if not soluciones_temp:
            print("    -> No se encontró solución entera no negativa para el sub-sistemas 3x3.")
            continue

        # Las soluciones encontradas a partir de las combinaciones 3x3 deben ser idénticas.
        # Además, todas deben satisfacer la 4ta ecuación (la que quedó fuera del 3x3).
        
        soluciones_unicas = sorted(list(set(soluciones_temp)))
        
        if len(soluciones_unicas) == 1:
            x, y, z = soluciones_unicas[0]
            
            # **Paso de Verificación Final (Consistencia):**
            # El único candidato (x, y, z) debe satisfacer *todas* las 4 ecuaciones asumidas como verdad.
            es_consistente = True
            for j in indices:
                a, b, c = preguntas[j]
                R_esperada = a * x + b * y + c * z
                R_obtenida = respuestas[j]
                
                if R_esperada != R_obtenida:
                    es_consistente = False
                    print(f"    -> Falló la verificación de consistencia en la ecuación {j+1}: {R_esperada} != {R_obtenida}")
                    break
            
            if es_consistente:
                if solucion_unica is not None and solucion_unica != (x, y, z):
                    # ¡Problema! Encontramos dos soluciones diferentes, el acertijo es ambiguo.
                    print(f"    -> ADVERTENCIA: Solución ambigua. Previa: {solucion_unica}, Nueva: {(x, y, z)}")
                    return "El acertijo es ambiguo, se encontraron múltiples soluciones consistentes."
                
                print(f"    -> SOLUCIÓN CONSISTENTE ENCONTRADA: Axex={x}, Basiliso={y}, Centauro={z}")
                solucion_unica = (x, y, z)
        else:
            # print(f"    -> Múltiples soluciones 3x3 inconsistentes o ninguna solución única: {soluciones_unicas}")
            pass

    return solucion_unica

# --- DATOS DEL EJEMPLO ---
# Incógnitas: x=Axex, y=Basiliso, z=Centauro
# Solución esperada: x=4, y=4, z=4

preguntas_ejemplo = [
    [1, 1, 1],  # P1: x + y + z
    [1, 1, 1],  # P2: x + y + z
    [5, 0, 1],  # P3: 5x + z
    [1, 0, 0],  # P4: x
    [1, 1, 0]   # P5: x + y
]

respuestas_ejemplo = [
    12,  # R1: 12 (Verdad)
    13,  # R2: 13 (Mentira, debería ser 12)
    24,  # R3: 24 (Verdad, 5*4 + 4 = 24)
    4,   # R4: 4 (Verdad, x=4)
    8    # R5: 8 (Verdad, 4 + 4 = 8)
]

# --- EJECUCIÓN ---
print("--- EJECUCIÓN DEL ACERTIJO DE LA ESFINGE ---")
print("Preguntas (a, b, c):", preguntas_ejemplo)
print("Respuestas (R):", respuestas_ejemplo)
print("-------------------------------------------\n")

resultado = resolver_acertijo_esfinge(preguntas_ejemplo, respuestas_ejemplo)

print("\n--- RESULTADO FINAL ---")
if isinstance(resultado, tuple):
    x, y, z = resultado
    print(f"¡La Esfinge ha sido derrotada!")
    print(f"Axex (x) = {x} patas")
    print(f"Basiliso (y) = {y} patas")
    print(f"Centauro (z) = {z} patas")
    
    # Identificar la mentira
    solucion_verdadera = np.array([x, y, z])
    for i in range(5):
        R_calculada = np.dot(np.array(preguntas_ejemplo[i]), solucion_verdadera)
        if R_calculada != respuestas_ejemplo[i]:
            print(f"La respuesta mentirosa fue la R{i+1}: {respuestas_ejemplo[i]} (el valor verdadero es {R_calculada})")
else:
    print(f"El acertijo no se pudo resolver con una solución única. Mensaje: {resultado}")