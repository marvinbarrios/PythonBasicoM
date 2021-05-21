peso = input("Ingrese peso en kilogramos: ")
estatura = input("Ingrese estatura en metros: ")
imc=round(float(peso)/float(estatura)**2,2)
print("El indice de masa corporal es:" , imc)
