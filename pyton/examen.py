prima_final = prima_base
    
    if edad < 21 and tipo_vehiculo.lower() == "deportivo":

        prima_final + = 1500
        justificacion.append("Incremento por edad menor a 21 y vehículo deportivo.")
    elif edad > 21 and años_sin_accidentes > 3:
        prima_final -= 1000
        justificacion.append("Descuento por edad mayor a 21 y más de 3 años sin accidentes.")

    resultado = f"Prima final:${prima_final}\nJustificación:"
    for j in justificacion:
        resultado += f"\n- {j}"

    if not justificacion:
        resultado += "\n- No se aplicaron ajustes especiales."

    return resultado
