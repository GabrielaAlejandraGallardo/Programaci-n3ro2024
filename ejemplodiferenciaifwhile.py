Sis="SI" #Defino la variable  "Sis" que dentro guarda la cadena de caracteres "SI"
Non="NO" #Defino la variable "Non" que dentro guarda la cadena de caracteres "NO"
Librería=["CARTULINA", "GOMA EVA", "PLASTICOLA", "LAPIZ", "MARCADORES"] #Creo una lista que guarda cada producto disponible en la sección de "LIBRERÍA"
Cocina=["OLLA", "BATIDORA", "CUBIERTOS", "UTENSILIOS DE COCINA"] #Creo una lista que guarda cada producto disponible en la sección de "COCINA"
Juguetería=["MUÑECAS", "AUTITOS", "JUEGOS DE COCINA", "JUGUETES SORPRESA"] #Creo una lista que guarda cada producto disponible en la sección de "JUGUETERÍA"
Bazar=["Juguetería", "Cocina", "Librería"] #Creo una lista que guarda cada sección disponible en el bazar
stock=["CARTULINA", "JUGUETES SORPRESA", "MUÑECAS", "AUTITOS", "BATIDORA", "CUBIERTOS", "MARCADORES", "LAPIZ", "OLLA"] #Creo la lista que contiene los elementos en stock
entrar=input("Bienvenido a nuestro bazar ¿desea  ingresar?: ") #Le pregunto al usuario si desea ingresar al bazar
entrar=entrar.upper()#Convierto la respuesta del cliente a mayúsculas para evitar problemas en el programa
JugueteríaC="JUGUETERIA" #Guardo en la varible "JugueteríaC" la cadena de caracteres "JUGUETERIA"
CocinaC="COCINA"#Guardo en la varible "CocinaC" la cadena de caracteres "COCINA"
LibreríaC="LIBRERIA"#Guardo en la varible "LibreríaC" la cadena de caracteres "LIBRERIA"
while entrar==Sis:
           print("Me alegra su interés en nuestros productos, estas son sus secciónes: ")
           print(Bazar)
           Buscar=input("¿Ya está decidido por su producto? ¿Desea buscarlo directamente?")
           Buscar=Buscar.upper()
           if Buscar=="SI":
                 Cat=input("Ingrese la categoría en la que se encuentra: ")
                 Cat=Cat.upper()
                 if Cat==JugueteríaC:
                       Cat=Cat.upper()
                       print(Juguetería)
                       Prod=input("Ingrese el producto que desea de los siguientes: ")
                       print("Usted debe consultar stock, un segundo por favor...")
                       Prod=Prod.upper()
                       if Prod in stock:
                             print("¡Su producto si está en stock, será empacado y está en camino!")
                       else:
                             print("El producto deseado no está en stock, por favor regrese más tarde")
                             print ("Le haremos un cuestionario, por favor responda sinceramente: ")
                             Add=input("1. ¿En qué categoría desería agregar un producto? : ")
                             Add=Add.upper()
                             Ad=input("2. ¿Qué elemento sería? : ")
                             Ad=Ad.upper()
                             if Add==JugueteríaC:
                                Juguetería.append(Ad)
                             elif Add==LibreríaC:
                                Librería.append(Ad)
                             elif Add==CocinaC:
                                Cocina.append(Ad)
                             catdel=input("¿De qué categoría eliminaría un elemento? : ")
                             catdel=catdel.upper()
                             elm=input("¿Cuál sería? : ")
                             elm=elm.upper()
                             if catdel==JugueteríaC:
                                 Juguetería.remove(elm)
                             elif catdel==LibreríaC:
                                 Librería.remove(elm)      
                             elif catdel==Cocina:
                                   Cocina.remove(elm)
                             elch=input("Debemos cambiar 'Juegos de cocina' por otro producto, ¿cuál elemento sería? : ")
                             elch=elch.upper
                             Juguetería[2]=elch
                             print("Así quedaría el catálogo: ", Juguetería, Cocina, Librería)      
                 elif Cat==CocinaC:
                       Cat=Cat.upper()
                       print(Cocina)
                       Prod=input("Ingrese el producto que desea de los siguientes: ")
                       print("Usted debe consultar stock, un segundo por favor...")
                       Prod=Prod.upper()
                       if Prod in stock:
                             print("¡Su producto si está en stock, será empacado y está en camino!")
                       else:
                             print("El producto deseado no está en stock, por favor regrese más tarde")
                 else:
                       Cat=Cat.upper()
                       print(Librería)
                       Prod=input("Ingrese el producto que desea de los siguientes: ")
                       print("Usted debe consultar stock, un segundo por favor...")
                       Prod=Prod.upper()
                       if Prod in stock:
                             print("¡Su producto si está en stock, será empacado y está en camino!")
                       else:
                             print("El producto deseado no está en stock, por favor regrese más tarde")
           else:
                print("Estas son las secciones de nuestro catálogo: ", Bazar)
                INT=input("¿Está interesado en alguna? (Ingrese la categoría): ")
                INT=INT.upper()
                if INT==JugueteríaC:
                       print("Estos son nuestros artículos en juguetería", Juguetería)
                       Tc=input("Si le interesa alguno toque '1' y toque '2' si desdea salir de la experiencia: ")
                       if Tc=="1":
                              pp=input("Ingrese el artículo que desea solicitar: ")
                              pp=pp.upper
                              if pp in stock:
                                    print("¡Su producto está en camino, muchas gracias!")
                              else:
                                    print("Su artículo deseado no está en stock, vuelva mas tarde...")
                              print ("Le haremos un cuestionario, por favor responda sinceramente: ")
                              Add=input("1. ¿En qué categoría desería agregar un producto? : ")
                              Add=Add.upper()
                              Ad=input("2. ¿Qué elemento sería? : ")
                              Ad=Ad.upper()
                              if Add==JugueteríaC:
                                 Juguetería.append(Ad)
                              elif Add==LibreríaC:
                                 Librería.append(Ad)
                              elif Add==CocinaC:
                                 Cocina.append(Ad)
                              catdel=input("¿De qué categoría eliminaría un elemento? : ")
                              catdel=catdel.upper()
                              elm=input("¿Cuál sería? : ")
                              elm=elm.upper()
                              if catdel==JugueteríaC:
                                  Juguetería.remove(elm)
                              elif catdel==LibreríaC:
                                  Librería.remove(elm)      
                              elif catdel==Cocina:
                                    Cocina.remove(elm)
                              elch=input("Debemos cambiar 'Juegos de cocina' por otro producto, ¿cuál elemento sería? : ")
                              elch=elch.upper
                              Juguetería[2]=elch
                              print("Así quedaría el catálogo: ", Juguetería, Cocina, Librería)      
                       else:
                             print ("Le haremos un cuestionario, por favor responda sinceramente: ")
                             Add=input("1. ¿En qué categoría desería agregar un producto? : ")
                             Add=Add.upper()
                             Ad=input("2. ¿Qué elemento sería? : ")
                             Ad=Ad.upper()
                             if Add==JugueteríaC:
                                Juguetería.append(Ad)
                             elif Add==LibreríaC:
                                Librería.append(Ad)
                             elif Add==CocinaC:
                                Cocina.append(Ad)
                             catdel=input("¿De qué categoría eliminaría un elemento? : ")
                             catdel=catdel.upper()
                             elm=input("¿Cuál sería? : ")
                             elm=elm.upper()
                             if catdel==JugueteríaC:
                                 Juguetería.remove(elm)
                             elif catdel==LibreríaC:
                                 Librería.remove(elm)      
                             elif catdel==Cocina:
                                   Cocina.remove(elm)
                             elch=input("Debemos cambiar 'Juegos de cocina' por otro producto, ¿cuál elemento sería? : ")
                             elch=elch.upper
                             Juguetería[2]=elch
                             print("Así quedaría el catálogo: ", Juguetería, Cocina, Librería)  
                elif INT==LibreríaC:
                       print("Estos son nuestros artículos en librería", Librería)
                       Tc=input("Si le interesa alguno toque '1' y toque '2' si desdea salir de la experiencia: ")
                       if Tc=="1":
                              pp=input("Ingrese el artículo que desea solicitar: ")
                              pp=pp.upper
                              if pp in stock:
                                    print("¡Su producto está en camino, muchas gracias!")
                              else:
                                    print("Su artículo deseado no está en stock, vuelva mas tarde...")
                       else:
                             print ("Le haremos un cuestionario, por favor responda sinceramente: ")
                             Add=input("1. ¿En qué categoría desería agregar un producto? : ")
                             Add=Add.upper()
                             Ad=input("2. ¿Qué elemento sería? : ")
                             Ad=Ad.upper()
                             if Add==JugueteríaC:
                                Juguetería.append(Ad)
                             elif Add==LibreríaC:
                                Librería.append(Ad)
                             elif Add==CocinaC:
                                Cocina.append(Ad)
                             catdel=input("¿De qué categoría eliminaría un elemento? : ")
                             catdel=catdel.upper()
                             elm=input("¿Cuál sería? : ")
                             elm=elm.upper()
                             if catdel==JugueteríaC:
                                 Juguetería.remove(elm)
                             elif catdel==LibreríaC:
                                 Librería.remove(elm)      
                             elif catdel==Cocina:
                                   Cocina.remove(elm)
                             elch=input("Debemos cambiar 'Juegos de cocina' por otro producto, ¿cuál elemento sería? : ")
                             elch=elch.upper
                             Juguetería[2]=elch
                             print("Así quedaría el catálogo: ", Juguetería, Cocina, Librería)  
                else:
                       print("Estos son nuestros artículos en cocina", Cocina)
                       Tc=input("Si le interesa alguno toque '1' y toque '2' si desdea salir de la experiencia: ")
                       if Tc=="1":
                              pp=input("Ingrese el artículo que desea solicitar: ")
                              pp=pp.upper
                              if pp in stock:
                                    print("¡Su producto está en camino, muchas gracias!")
                              else:
                                    print("Su artículo deseado no está en stock, vuelva mas tarde...")  
                              print ("Le haremos un cuestionario, por favor responda sinceramente: ")
                              Add=input("1. ¿En qué categoría desería agregar un producto? : ")
                              Add=Add.upper()
                              Ad=input("2. ¿Qué elemento sería? : ")
                              Ad=Ad.upper()
                              if Add==JugueteríaC:
                                 Juguetería.append(Ad)
                              elif Add==LibreríaC:
                                 Librería.append(Ad)
                              elif Add==CocinaC:
                                 Cocina.append(Ad)
                              catdel=input("¿De qué categoría eliminaría un elemento? : ")
                              catdel=catdel.upper()
                              elm=input("¿Cuál sería? : ")
                              elm=elm.upper()
                              if catdel==JugueteríaC:
                                 Juguetería.remove(elm)
                              elif catdel==LibreríaC:
                                 Librería.remove(elm)      
                              elif catdel==Cocina:
                                   Cocina.remove(elm)
                              elch=input("Debemos cambiar 'Juegos de cocina' por otro producto, ¿cuál elemento sería? : ")
                              elch=elch.upper
                              Juguetería[2]=elch
                              print("Así quedaría el catálogo: ", Juguetería, Cocina, Librería)      
                       else:
                             print ("Le haremos un cuestionario, por favor responda sinceramente: ")
                             Add=input("1. ¿En qué categoría desería agregar un producto? : ")
                             Add=Add.upper()
                             Ad=input("2. ¿Qué elemento sería? : ")
                             Ad=Ad.upper()
                             if Add==JugueteríaC:
                                Juguetería.append(Ad)
                             elif Add==LibreríaC:
                                Librería.append(Ad)
                             elif Add==CocinaC:
                                Cocina.append(Ad)
                             catdel=input("¿De qué categoría eliminaría un elemento? : ")
                             catdel=catdel.upper()
                             elm=input("¿Cuál sería? : ")
                             elm=elm.upper()
                             if catdel==JugueteríaC:
                                 Juguetería.remove(elm)
                             elif catdel==LibreríaC:
                                 Librería.remove(elm)      
                             elif catdel==Cocina:
                                   Cocina.remove(elm)
                             elch=input("Debemos cambiar 'Juegos de cocina' por otro producto, ¿cuál elemento sería? : ")
                             elch=elch.upper
                             Juguetería[2]=elch
                             print("Así quedaría el catálogo: ", Juguetería, Cocina, Librería)      
print("Saliendo del sistema")                                          




