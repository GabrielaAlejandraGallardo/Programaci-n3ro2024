l=[]
while True:#condición a evaluar
    opcion=input("Menú de opciones\n1-Agregar producto\n2-Eliminar producto\n3-Modificar productor\n4-Mostar productos\n5-Salir \n")
    if opcion=="1":
         elementoAgregar=input("Ingrese elemento a agregar:")
         l.append(elementoAgregar)
    elif opcion=="2":
        elementoAeliminar=input("Ingrese el nombre del elemento a modificar: ")
        if elementoAeliminar in l:
           l.remove(elementoAeliminar)
           print("Elemento eliminado exitosamente")    
        else:
            print("El elemento que desea eliminar no se encuentra en la lista")       
    elif opcion=="3":
        elementoAmodificar=input("Ingrese el nombre del elmento a modificar: ")
        if elementoAmodificar in l:
            elementoModificacion=input("Ingrese el nombre por el que quiere modificar: ")
            # Find the index of the element to modify
            index = l.index(elementoAmodificar) 
            print("elemento a cambiar:", index)
            l[index] = elementoModificacion # Use the index to modify the element
        else:
            print("El elemento que desea modificar no se encuentra en la lista")
            
    elif opcion=="4":
        print("Elementos en la lista: \n",l)    
    elif opcion=="5":            
        print("Saliendo del sistema")
        break
    else:
        print("La opción ingresada es invalida")    
    
