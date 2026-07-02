usuarios = ["Aldrin 777", "maicol 67", "maria 1234","kike IA"]
print("sistema iniciado y sin ia")
while True:
 
 input_usuario = input("Ingresa tu nombre de usuario: ")
 print("Bienvenido", input_usuario)
 if input_usuario == "Aldrin 777":
    opcin = input("¿que accion desea realizar? ")
    if opcin == "ver otras cuentas":
         for nombre in usuarios:
            print(nombre)
           
    elif opcin == "importar calculadora":
        import calculadora

    else:
        print("Gracias por visitarnos, hasta luego")                                                              

    
 elif input_usuario in usuarios:
    
    print("tienes una funcion usar la calculadora")
    opcin = input("¿que accion desea realizar? ")
    if opcin == " calculadora":
        import calculadora

 else:
    print("Usuario no encontrado.")
    input_respuesta = input("¿Deseas crear una cuenta? (si/no): ")
    if input_respuesta == "si":
        nuevo_usuario = input("Ingresa tu nuevo nombre de usuario: ")
        usuarios.append(nuevo_usuario)
        print("Cuenta creada exitosamente, bienvenido", nuevo_usuario)
    else:
        print("Gracias por visitarnos, hasta luego")
palabras = ("lo hice yo solito y sin ayuda de nadie y sin usar ninguna herramienta de inteligencia artificial pero ojo hay que entender que copilot lo uso pero"
            "solo para corregir errores de sintaxis y no para escribir codigo ni nada por el estilo solo para corregir errores de sintaxis y nada mas o tambien lo uso para"
            "poner cosas mas rapido pero solo admito lo que conosco como se ve en este video gracias : > bye" )