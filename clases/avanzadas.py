class Calculadora:
    def potencia(self):
        try:
            base = float(input("Ingresa la base: "))
            exponente = float(input("Ingresa el exponente: "))
            resultado = base ** exponente
            print(f"Resultado: {resultado}")
        except ValueError:
            print("Error: Debes ingresar números válidos.")

    def raiz(self):
        try:
            numero = float(input("Ingresa el número: "))
            if numero < 0:
                print("Error: No se puede calcular la raíz de un número negativo.")
                return
            resultado = numero ** 0.5
            print(f"Resultado: {resultado}")
        except ValueError:
            print("Error: Debes ingresar un número válido.")
