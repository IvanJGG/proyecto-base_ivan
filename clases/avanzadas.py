class Calculadora:
    def potencia(self):
        try:
            base = float(input("Ingresa la base: "))
            exponente = float(input("Ingresa el exponente: "))
            resultado = base ** exponente
            print(f"Resultado: {resultado}")
        except ValueError:
            print("Error: Debes ingresar números válidos.")
