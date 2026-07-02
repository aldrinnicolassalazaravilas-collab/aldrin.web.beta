usuarios = ["wasa"]


while True:


 nombre = input("Ingresa tu nombre de usuario: ")

 if nombre in usuarios:
        print("Bienvenido", nombre)
 elif nombre == "Aldrin 7778":
            pregunta = input("¿Quieres ver las demas cuentas? (si/no): ")
            for nombre in usuarios:
                print(nombre)
 else:
        print("No encontramos tu cuenta")

        respuesta = input("¿Quieres crear una cuenta? (si/no): ")

        if respuesta == "si":
            nombre = input("Ingresa tu nuevo nombre de usuario: ")
 
            usuarios.append(nombre)
            print("Cuenta creada exitosamente, bienvenido", nombre)

        
                
        else:
            print("Gracias por visitarnos, hasta luego")
