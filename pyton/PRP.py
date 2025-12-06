import math 
k = 8.617e-5  
materiais = {
    "silicio": {"Eg": 1.1, "tipo": "semi condutor"},
    "arseniuro de gálio": {"Eg": 1.43, "tipo": "semi condutor"},
    "germanio": {"Eg": 0.66, "tipo": "semi condutor"},
    "cobre": {"Eg": 5.2e-19, "tipo": "condutor"},
    "vidro": {"Eg": 9.0, "tipo": "isolante"}
}
def silicio():
    Eg = materiais["silicio"]["Eg"]
    T = 300
    n_i = 2.5e15 * (T / 300)**1.5 * math.exp(-Eg / (2 * k * T))
    print("n_i do silício é:", n_i, "electrons/cm^3 (aprox. independente de T)")
def arseniuro_de_galio():
    Eg = materiais["arseniuro de gálio"]["Eg"]
    T = 300
    n_i = 2.5e15 * (T / 300)**1.5 * math.exp(-Eg / (2 * k * T))
    print("n_i do arseniuro de gálio é:", n_i, "electrons/cm^3 (aprox. independente de T)")
material = input("Digite o material (silicio/arseniuro de gálio): ").lower()
T = int(input("Digite a temperatura (K): "))


if material in materiais:
    Eg = materiais[material]["Eg"]
    n_i = 2.5e15 * (T / 300)**1.5 * math.exp(-Eg / (2 * k * T))
    print("Densidade intrínseca de portadores (n_i):", n_i, "electrons/cm^3")
else:
    print("Material inválido")
