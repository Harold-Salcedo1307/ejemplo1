
def multiplicar(a, b):
    return a * b

def dividir(a, b):
    if b == 0:
        return "Error: No se puede dividir entre cero."
    return a / b

def calculadora():
    print("--- CALCULADORA BÁSICA ---")
    print("Selecciona una operación:")
    print("3. Multiplicación")
    print("4. División")

    opcion = input("Introduce el número de la operación (3/4): ")

    if opcion in ('3', '4'):
        try:
            num1 = float(input("Introduce el primer número: "))
            num2 = float(input("Introduce el segundo número: "))
        except ValueError:
            print("Error: Por favor, introduce solo números válidos.")
            return
        if opcion == '3':
            print(f"Resultado: {num1} * {num2} = {multiplicar(num1, num2)}")
        elif opcion == '4':
            print(f"Resultado: {num1} / {num2} = {dividir(num1, num2)}")
    else:
        print("Opción no válida. Por favor, elige una opción entre 1 y 4.")

# Ejecutar la calculadora
calculadora()
