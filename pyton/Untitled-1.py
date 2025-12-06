import numpy as np
from itertools import combinations

def resolver_acertijo_esfinge_algebraico():
    """
    Resuelve el acertijo de la Esfinge usando Álgebra Lineal (NumPy) para 
    identificar la respuesta mentirosa y encontrar la solución (x, y, z).
    """
    print(" SOLUCIONADOR ALGEBRAICO DE LA ESFINGE")
    print("El programa te pedirá las 5 respuestas a las preguntas definidas.\n")

    A_preguntas = np.array([
        [1, 0, 0],  # Ecuación 1: x
        [0, 1, 0],  # Ecuación 2: y
        [0, 0, 1],  # Ecuación 3: z
        [1, 1, 1],  # Ecuación 4: x + y + z
        [1, 2, 3]   # Ecuación 5: x + 2y + 3z
    ])
    
    R_respuestas = []

   
    for i in range(5):
        a, b, c = A_preguntas[i]
        print(f"PREGUNTA {i+1}: ¿Cuántas patas tienen {a} axexes, {b} basiliscos y {c} centauros?")
        while True:
            try:
                val = int(input(f"   >> Respuesta de la Esfinge para la pregunta {i+1}: "))
                if val < 0:
                    print("   Por favor, ingresa un número no negativo.")
                    continue
                R_respuestas.append(val)
                break
            except ValueError:
                print("   Por favor, ingresa un número entero válido.")

    R_respuestas = np.array(R_respuestas)
    print("\nCalculando la única verdad consistente...\n")

   
    solucion_final = None
    mentira_indice = -1

  
    for i in range(5):
        
        indices_verdad = [j for j in range(5) if j != i]
        
        
        A_verdad = A_preguntas[indices_verdad]
        R_verdad = R_respuestas[indices_verdad]
        
       
        for sub_indices_list in combinations(range(4), 3):
           
            A_3x3 = A_verdad[np.array(sub_indices_list)]
            R_3x1 = R_verdad[np.array(sub_indices_list)]
            
            
            if np.linalg.det(A_3x3) == 0:
                continue

            try:
               
                X = np.linalg.solve(A_3x3, R_3x1)
                
                
                x, y, z = X
                if all(val.is_integer() and val >= 0 for val in X):
                    
                    x, y, z = map(int, X)
                    
                    
                    es_consistente = True
                    for j in indices_verdad:
                        a, b, c = A_preguntas[j]
                        R_esperada = a * x + b * y + c * z
                        if R_esperada != R_respuestas[j]:
                            es_consistente = False
                            break
                            
                    if es_consistente:
                       
                        solucion_final = (x, y, z)
                        mentira_indice = i + 1
                        break 
                        
            except np.linalg.LinAlgError:
                continue 
        
        if solucion_final:
            break 

    
    if solucion_final:
        ax, ba, ce = solucion_final
        print("-" * 30)
        print("¡SOLUCIÓN ENCONTRADA! (Mentira = Pregunta #%d)" % mentira_indice)
        print("-" * 30)
        print(f"Axexes     : {ax} patas")
        print(f"Basiliscos : {ba} patas")
        print(f"Centauros  : {ce} patas")
        print("-" * 30)
        
        val_real = R_respuestas[mentira_indice-1]
        a, b, c = A_preguntas[mentira_indice-1]
        val_calc = (a * ax) + (b * ba) + (c * ce)
        print(f"La Esfinge mintió en la **Pregunta #{mentira_indice}**.")
        print(f"Dijo '{val_real}', pero el valor verdadero es '{val_calc}'.")

    else:
        print("❌ No se encontró una solución lógica única y consistente.")
        print("Verifica que solo una de las 5 respuestas sea incorrecta.")


if __name__ == "__main__":
   
    resolver_acertijo_esfinge_algebraico()