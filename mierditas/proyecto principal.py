import os
import time

historial = []

while True:
    pregunta = input("¿que accion quieres realizar? escribe acciones para ver las acciones disponibles:")
    historial.append(pregunta)
    if pregunta == "acciones":
        print("saludar,sumar,iniciar web,ver la hora,salir,ver historial")
        print("estas acciones solo se escribien la palabra al momento que el programa  te diga  = ¿que accion quieres realizar? y esta se ejecutara al momento que la escribas")
    elif pregunta == "saludar":
        nombre = input("¿cual es tu nombre?: ")
        print("hola ", nombre, "bienvenido a mi programa")                                       
    elif pregunta == "sumar":
        numero1 = int(input("dime un numero: "))
        numero2 = int(input("dime otro numero: "))
        resultado = numero1 + numero2
        print("el resultado de la suma es: ", resultado)   
    elif pregunta == "iniciar web":
        confirmacion = input("¿quieres iniciar la pagina web? (si/no): ")
        if confirmacion.lower() == "si":
            print("Iniciando servidor web desde app.py...")
            # Esto intentará ejecutar el archivo app.py
            os.system("python app.py")
        else:
            print("no se iniciara la pagina web")
    
    elif pregunta == "ver la hora":
        print(time.ctime())    
    elif pregunta == "salir":
        print("gracias por usar mi programa, hasta luego")
        break   
    elif pregunta == "ver historial":
        if not historial:
            print("No hay acciones en el historial.")
        else:
            print("--- Historial de acciones ---")
            for i, accion in enumerate(historial):
                print(f"{i+1}. {accion}")
            print()