import math

k = 8.617e-5  

Eg = {
    "Si": 1.12,   
    "Ge": 0.66,   
    "GaAs": 1.43  
}
A = {
    "Si": 5.2e15,
    "Ge": 1.6e15,
    "GaAs": 2.1e15
}

print("Materiales disponibles: Si, Ge, GaAs")

material = input("Elige material: ").strip()
if material not in Eg:
    print(" Material no encontrado. Usa Si, Ge o GaAs.")
else:
    T = float(input("Temperatura en K: "))

    ni = A[material] * (T**1.5) * math.exp(-Eg[material] / (2 * k * T))

    print("\n-")
    print(f"Material: {material}")
    print(f"Temperatura: {T:.1f} K")
    print(f"ni = {ni:.3e} electrones/cm³")
    print("-")