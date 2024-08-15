lados=int(input("Ingrese la cantidad de lados de la figura:"))
if lados==4:
    l1=int(input("Ingrese el valor del primer lado:"))
    l2=int(input("Ingrese el valor del segundo lado:"))
    l3=int(input("Ingrese el valor del tercer lado:"))
    l4=int(input("Ingrese el valor del cuarto lado:"))
    
    if l1==l2 and l1==l3 and l1==l4:
        print("La figura podrá ser un cuadrado o rombo")
    elif l1!=l3 or l2!=l4:
        print("La figura podrá ser un rectangulo trapezoide escaleno")  
    elif l1==l3 and l2==l4:      
        print("La figura geométrica es un rectangulo o paralelogramo")
elif lados==3:
    print("La figura geométrica es un triángulo")
         
      
      
      
      