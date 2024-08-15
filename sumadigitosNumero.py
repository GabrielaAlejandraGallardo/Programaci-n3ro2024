n=input("Ingrese un número para sumar sus digitos:")
suma=0
lista=list(n)
for digito in lista:
    suma=suma+int(digito)
print(suma)    