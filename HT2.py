# Ejercicio 1

triangulo = int(input("Ingrese un numero entero mayor a 0: "))
if triangulo<=0:
    print("el numero ingresado no es un numero valido")
else:
    for contador1 in range(triangulo):
        for contador2 in range(contador1+1):
            print("*", end="")
        print("")


# Ejercicio 2

cuenta = int(input("Ingrese un numero entero mayor a 0: "))
if cuenta<=0:
    print("el numero ingresado no es un numero valido")
else:
    i=0
    while i<=cuenta:
        print(str(cuenta)+", ", end="")
        cuenta-=1
    print("")


# Ejercicio 3

primo=int(input("Ingrese un numero entero mayor que 2: "))
i=2
if primo<=2:
    print("el numero ingresado no es un numero valido")
else:
    while primo%i!=0:
        i+=1
    if i==primo:
        print(str(primo)+" es primo")
    else:
        print(str(primo)+" no es primo")