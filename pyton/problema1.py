def resolver_acertijo_esfinge():
    print(" SOLUCIONADOR DEL ACERTIJO DE LA ESFINGE ")
    print("El programa te dirá qué preguntar. Introduce la respuesta que te dé la Esfinge.\n")

    
    preguntas = [
        (1, 0, 0),  # Pregunta 1: Solo Axexes
        (0, 1, 0),  # Pregunta 2: Solo Basiliscos
        (0, 0, 1),  # Pregunta 3: Solo Centauros
        (1, 1, 1),  # Pregunta 4: Suma de todos
        (1, 2, 3)   # Pregunta 5: Suma ponderada para desempatar
    ]

    respuestas = []

   
    for i, (a, b, c) in enumerate(preguntas, 1):
        print(f"PREGUNTA {i}: ¿Cuántas patas tienen {a} axexes, {b} basiliscos y {c} centauros?")
        while True:
            try:
                val = int(input(f"   >> Respuesta de la Esfinge para la pregunta {i}: "))
                if val < 0:
                    print("   Por favor ingresa un número no negativo.")
                    continue
                respuestas.append(val)
                break
            except ValueError:
                print("   Por favor ingresa un número entero válido.")

    print("\nCalculando la verdad detrás de la mentira...\n")

   
    
    solucion_encontrada = None
    mentira_detectada = -1
    
    
    rango_busqueda = range(101) 

    found = False
    for x in rango_busqueda:       
        if found: break
        for y in rango_busqueda:   
            if found: break
            for z in rango_busqueda: 
                
                
                coincidencias = 0
                indice_fallo = -1
                
                for i, (a, b, c) in enumerate(preguntas):
                    teorico = (a * x) + (b * y) + (c * z)
                    if teorico == respuestas[i]:
                        coincidencias += 1
                    else:
                        indice_fallo = i + 1 
                
               
                if coincidencias >= 4:
                    solucion_encontrada = (x, y, z)
                    mentira_detectada = indice_fallo if coincidencias == 4 else 0
                    found = True
                    break

   
    if solucion_encontrada:
        ax, ba, ce = solucion_encontrada
        print("-" * 30)
        print("¡SOLUCIÓN ENCONTRADA!")
        print("-" * 30)
        print(f"Axexes     : {ax} patas")
        print(f"Basiliscos : {ba} patas")
        print(f"Centauros  : {ce} patas")
        print("-" * 30)
        
        if mentira_detectada > 0:
            print(f"Detecté que la Esfinge mintió en la Pregunta #{mentira_detectada}.")
            val_real = respuestas[mentira_detectada-1]
            # Recalcular el valor real
            a,b,c = preguntas[mentira_detectada-1]
            val_calc = (a*ax) + (b*ba) + (c*ce)
            print(f"Dijo '{val_real}', pero la verdad matemática es '{val_calc}'.")
        else:
            print("La Esfinge no mintió en ninguna pregunta (o la mentira fue coincidente).")
            
    else:
        print("No se encontró una solución lógica consistente.")
        print("Asegúrate de haber copiado bien las respuestas de la Esfinge.")

if __name__ == "__main__":
    resolver_acertijo_esfinge()