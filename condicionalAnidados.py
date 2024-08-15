rta="si"
while rta=="si":
    opcion=int(input("MENÚ OPCIONES \n 1 decir hola. \n 2 decir chau \n 3 decir espere \n"))
    if opcion==1:
       print("hola")
    elif opcion==2:
        print("chau")
    elif  opcion==3:
        print("Espere    ")
    else:
        print("Opción invalida")    
    rta=input("Desea volver al menú? si o no: ")    