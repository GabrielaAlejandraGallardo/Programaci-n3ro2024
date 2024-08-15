temperatura=float(input("Ingrese la temperatura actual:"))
menuPlatosfrios=["Ensalada completa","Ensalada Cesar"]
menuPlatosCalientes=["Polenta","Guiso"]
if temperatura>=25:
    print("El menú sugerido para este tiemppo de calor es:",menuPlatosfrios)
else:
      print("El menú sugerido para este tiemppo de frio es:",menuPlatosCalientes)
        