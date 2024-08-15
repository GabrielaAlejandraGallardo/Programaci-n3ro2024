prod=[]
rta="Si"


while rta=="Si" or rta=="si" or rta=="SI":
    opcion=input("Seleccione una opción \n 1.Agregar productos a la lista \n 2-Mostrar prodcutos en la lista \n 3.Salir \n " )
    if opcion=="1":
        productoAgregar=input("Ingrese el nombre del producto a agregar a la lista: ")
        prod.append(productoAgregar)
    elif opcion=="2":
        print("Los productos en la lista son:\n _________________________________")
        for p in prod:
            print(p,"\n _________________________________")     
           
    elif opcion=="3":
        rta=input("Desea cntinuar en el sistema si/no: ")
        if rta=="no" or rta=="NO" or rta=="No":
            print("Saliendo del sistema")     
    else:
        print("Ingreso una opción no válida")        