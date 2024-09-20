import time
# def programa():
#     palabra =str(input("ingrese una palabra "))
#     cantidad =int(input("ingrese una cantidad "))
#     for i in range(cantidad):
#         print("valor de la variable i ", i+1)
#         time.sleep(2)
#         print(palabra)
#     return palabra
# programa()

# def edad():
#     edad = int(input("ingrese su edad "))
#     for i in range(edad): 
#         print(i+1)
#     return edad
# edad()
# def calcular_edad():
#     añoActual= int(input("ingrese el año actual"))
#     AñoNacimiento= int(input("ingrese el año nacimiento"))
#     edad = añoActual-AñoNacimiento
#     for i in range(edad):
#         print(AñoNacimiento+i +1)
#         print(i+1)
#         time.sleep(1)
#     return edad
# calcular_edad()

# def numeros_impares():
#     numero = int(input("ingrese un numero "))
#     for i in range(1,numero+1,2):
#         time.sleep(1)
#         print(i, end=" , ")
#         if i == 15:
#             break;
# numeros_impares()

def reloj():
    tiempoMax= int(input("ingrese el tiempo maximo "))
    for i in range(1,60+1):
        print(i)
        if i == tiempoMax:
            print("Tiempo maximo", tiempoMax )
            break;
                             
# reloj()
def calcular_inte():
    cantidad = float(input("ingrese la cantidad "))
    I_An = float(input("ingrese el interes anual "))
    Año = int(input("ingrese el año "))
    for i in range(1, Año+1):
        interes = cantidad*(I_An/100)
        resultado = cantidad+interes
        print(f"El valor en el año {i} es: {resultado} ")
# calcular_inte()

def calcular():
    numero = int(input("ingrese un numero "))
    for i in range(1, numero+1):
        print("*" *i)
# calcular()

def descrubir_contraseña():
    contraseña = "123456789"
    contraseña_ingresada = ""
    intento_ingresado = int(input("ingrese el numero de intentos "))
    intento = 1
    while contraseña_ingresada != contraseña:
        contraseña_ingresada = str(input("ingrese la contraseña: "))
        if contraseña_ingresada != contraseña:
            print("la contraseña no coincide")
        elif contraseña_ingresada == contraseña:
            print("contraseña correcta")
            return
        if intento == intento_ingresado:
            print("se llego al limite de intentos")
            intento += 1
            break;
        intento += 1
# descrubir_contraseña()
def contador_letra():
    frase=(str(input("Ingresa una frase")))
    letra=(str(input("Ingrese una letra")))
    cont_letra=0
    for i in frase:
        if letra == i:
            cont_letra +=1
    print("la letra", letra, "se repite",cont_letra, "veces")
    
contador_letra()
        
