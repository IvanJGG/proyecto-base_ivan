from clases.avanzadas import Calculadora

def main():
    calc = Calculadora()
    
    while True:
        print("\n--- Calculadora ---")
        print("1. Potencia")
        print("2. Raíz")
        print("3. Salir")
        
        opcion = input("Elige una opción: ")

        if opcion == "1":
            calc.potencia()
        elif opcion == "2":
            calc.raiz()
        elif opcion == "3":
            print("Saliendo...")
            break
        else:
            print("Opción no válida.")

if __name__ == "__main__":
    main()
