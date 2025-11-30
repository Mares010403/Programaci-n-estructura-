import sys

def resolver_mosaico():

    
    print("Introduce las dimensiones del MOTIVO (filas columnas):")
    try:
        linea1 = sys.stdin.readline().split()
        if not linea1: return # Fin de entrada
        R_motivo, C_motivo = map(int, linea1)
    except ValueError:
        print("Error en formato de dimensiones.")
        return

    print("Introduce la matriz del MOTIVO:")
    motivo = []
    for _ in range(R_motivo):
        motivo.append(list(map(int, sys.stdin.readline().split())))

    print("Introduce las dimensiones del MOSAICO (filas columnas):")
    R_mosaico, C_mosaico = map(int, sys.stdin.readline().split())

    print("Introduce la matriz del MOSAICO:")
    mosaico = []
    for _ in range(R_mosaico):
        mosaico.append(list(map(int, sys.stdin.readline().split())))

    
    puntos_a_verificar = []
    for r in range(R_motivo):
        for c in range(C_motivo):
            if motivo[r][c] != 0:
                puntos_a_verificar.append((r, c, motivo[r][c]))

  
    coincidencias = []

    
    limite_filas = R_mosaico - R_motivo + 1
    limite_cols = C_mosaico - C_motivo + 1

    for r in range(limite_filas):
        for c in range(limite_cols):
            match = True
            
            for pr, pc, valor in puntos_a_verificar:
               
                mosaico_r = r + pr
                mosaico_c = c + pc
                
                if mosaico[mosaico_r][mosaico_c] != valor:
                    match = False
                    break 
            
            if match:
                
                coincidencias.append((r + 1, c + 1))

   
    print("\n--- RESULTADOS ---")
    print(f"Número de coincidencias: {len(coincidencias)}")
    print("Lista de posiciones (fila, columna):")
    for pos in coincidencias:
        print(f"{pos[0]}, {pos[1]}")

if __name__ == "__main__":
    resolver_mosaico()