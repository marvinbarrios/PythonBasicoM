# Ejercicio 1

contraseña = input("Ingresar la contraseña a guardar: ")
validacion = input("Ingresar nuevamente la contraseña para validar que coincide: ")
if validacion==contraseña:
    print("La contraseña coincide con la contraseña guardada")
else:
    print("La contraseña no coincide")


# Ejercicio 2

nombre = input("Ingrese primer nombre: ")
sexo = input("Ingrese sexo (M o F): ")
if sexo.lower()=="f":
    if nombre.lower()<="m":
        grupo="A"
    else:
        grupo="B"
else:
    if nombre.lower()>="n":
        grupo="A"
    else:
        grupo="B"
print("Corresponde al grupo: " + grupo)
