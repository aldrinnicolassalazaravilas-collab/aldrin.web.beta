def suma():
    suma_numero1 = int(input("Ingrese el primer número: "))
    suma_numero2 = int(input("Ingrese el segundo número: "))
    suma_resultado = suma_numero1 + suma_numero2
    print("El resultado de la suma es:", suma_resultado)

def resta():
    resta_numero1 = int(input("Ingrese el primer número: "))
    resta_numero2 = int(input("Ingrese el segundo número: "))
    resta_resultado = resta_numero1 - resta_numero2
    print("El resultado de la resta es:", resta_resultado)
def multiplicacion():
    multiplicacion_numero1 = int(input("Ingrese el primer número: "))
    multiplicacion_numero2 = int(input("Ingrese el segundo número: "))
    multiplicacion_resultado = multiplicacion_numero1 * multiplicacion_numero2
    print("El resultado de la multiplicación es:", multiplicacion_resultado)
def division():
    division_numero1 = int(input("Ingrese el primer número: "))
    division_numero2 = int(input("Ingrese el segundo número: "))
    if division_numero2 != 0:
        division_resultado = division_numero1 / division_numero2
        print("El resultado de la división es:", division_resultado)
    else:
        print("Error: No se puede dividir por cero.")   



while True:
    print("Bienvenido a la calculadora")
    pregunta = input("¿Qué operación desea realizar? (suma, resta, multiplicación, división) o 'salir' para terminar: ")
    if pregunta == "suma":
     suma()

    elif pregunta == "resta":
     resta()

    elif pregunta == "multiplicación":
     multiplicacion()

    elif pregunta == "división":
     division()

    elif pregunta == "salir":
     print("Gracias por usar la calculadora.")
     break