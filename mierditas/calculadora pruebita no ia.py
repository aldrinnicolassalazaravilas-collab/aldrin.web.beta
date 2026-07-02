def suma():
    numero_1_suma = int(input("Dime un número: "))
    numero_2_suma = int(input("Dime otro número: "))
    resultado = numero_1_suma + numero_2_suma
    print("El resultado de la suma es:", resultado)
    print("el resultado de la suma es:", resultado)   
def resta():
    numero_1_resta = int(input("Dime un número: "))
    numero_2_resta = int(input("Dime otro número: "))
    resultado = numero_1_resta - numero_2_resta
    print("El resultado de la resta es:", resultado)    
def multiplicacion(): 
    numero_1_multiplicacion = int(input("Dime un número: "))
    numero_2_multiplicacion = int(input("Dime otro número: "))
    resultado = numero_1_multiplicacion * numero_2_multiplicacion
    print("El resultado de la multiplicación es:", resultado)
    
while True:
    pregunta = input("¿Qué operación deseas realizar? (suma, resta, multiplicación) o 'salir' para terminar: ")
    if pregunta == "suma":
     suma()
    elif pregunta == "resta":
     resta()
    elif pregunta == "multiplicación":
     multiplicacion()
    elif pregunta == "salir":      
     print("Gracias por usar la calculadora.")
     break
