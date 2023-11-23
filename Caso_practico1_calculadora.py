def sumar(x, y):
    return x + y


def restar(x, y):
    return x - y


def multiplicar(x, y):
    return x * y


def dividir(x, y):
    if y != 0:
        return x / y
    else:
        return "Error"


def potencia(x, y):
    return x**y


def raiz_cuadrada(x):
    if x >= 0:
        return x**0.5
    else:
        return "Error"


def calculadora():
    print("¡Bienvenido a la Calculadora!")
    while True:
        eleccion = input(
            "Selecciona una operación (Sumar(1) / Restar(2) / Multiplicar(3) / Dividir(4) / Potencia(5) / Raiz cuadrada(6) / Salir(7)): "
        )
        if eleccion == "7":
            break
        elif eleccion in ["1", "2", "3", "4", "5"]:
            x = int(input("Introduce el primer numero: "))
            y = int(input("Introduce el segundo numero: "))
            if eleccion == "1":
                result = sumar(x, y)
            elif eleccion == "2":
                result = restar(x, y)
            elif eleccion == "3":
                result = multiplicar(x, y)
            elif eleccion == "4":
                result = dividir(x, y)
            elif eleccion == "5":
                result = potencia(x, y)
            print(f"El resultado es: {result}")
        elif eleccion == "6":
            x = float(input("Numero sobre el que realizar raiz: "))
            result = raiz_cuadrada(x)
            print(f"El resultado es: {result}")
        else:
            print(f"{eleccion} Opción no válida")


if __name__ == "__main__":
    calculadora()
