contador=0
start=True
Usuario=(input("Ingrese su nombre de usuario: "))
contraseña=(input("Ingrese una contraseña: "))
error="no"
while start==True:
   contador=contador+1
   Usuarioin=(input("Ingrese su nombre de usuario: "))
   Contraseñain=(input("Ingrese la contraseña: "))
   if Usuario==Usuarioin and contraseña==Contraseñain:
       print("Usuario y contraseña correctos, bienvenido")
       break
   else:
       print("Usuario o contraseña incorrectos, por favor dejenos analizar más a profundidad... ")
       error="si"


   if error=="si":
      if Usuario==Usuarioin:
         print("error en la contraseña, intente de nuevo")
      elif contraseña==Contraseñain:
          print ("error en el usuario, intente de nuevo")
      else:
          print("error en ambos valores, intente de nuevo")
   
           
   print ("Usted va por el intento N° ", contador, "/3")
   if contador==3:
       print("Su cuenta ha sido bloqueada")
       break
