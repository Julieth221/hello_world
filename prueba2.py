# def suma(a, b):
#     global result
#     result = a + b
#     return result
# suma(4, 5)
# print ("primera suma")
# print (result)
# suma(1,2)
# print ("segunda suma")
# print(result)
# def calculadora_dos_valores(num1, num2, operador):
#     global result
#     if operador == "+":
#         result = num1 + num2 
#         return result
#     elif operador == "-":
#         result = num1 - num2 
#         return result
#     elif operador == "*":
#         result = num1 * num2 
#         return result
#     elif operador == "/":
#         if num2 != 0:
#             result = num1 / num2 
#             return result
#         else:
#             return "Error: División por cero"
#     else:
#         return "Error: Operador no válido"
    
# calculadora_dos_valores(1,2,"+")
# print("suma", result)
# calculadora_dos_valores(1,2,"-")
# print("resta", result)
# calculadora_dos_valores(1,2,"*")
# print("multiplicacion", result)
# calculadora_dos_valores(1,2,"/")
# print("division", result)
# import math
# def cal_pitagoras(a,b):
#     global result
#     result = math.sqrt ((a**2) + (b**2))
#     return result
# cal_pitagoras(2,4)
# print(result)

# def pitagoras_funcion_sumar():
#     global result
#     a= int(input("ingrese el valor de A "))
#     b= int(input("ingrese el valor de B "))
#     a2 = a **2
#     b2 = b ** 2
#     sumar = suma(a2,b2)
#     result = sumar**0.5
#     print("el valor de pitagoras es: ", result)
#     return result
# pitagoras_funcion_sumar()

# def depejeX ():
#     global x
#     b= int(input("ingrese el valor de B "))
#     c= int(input("ingrese el valor de C "))
#     x = (c-b)/2
#     print("el valor de x es: ", x)
#     return x

# depejeX()

# def compuerta_and():
#     global X
#     a= bool(input("ingrese el valor a "))
#     print(a)
#     b= bool(input("ingrese el valor b "))
#     c= bool(input("ingrese el valor c ")) 
#     X = a*b*c
#     print(X)
#     return X
# compuerta_and()
# def palabra():
#     global result
#     word=(str(input("ingrese una palabra: ")))
#     letter=(str(input("ingrese la letra: ")))
#     cont_letter =word.count(letter)
#     print("la cantidad de letras ", letter, "es: ",cont_letter)
#     print("cantidad de caracteres: ", len(word))
#     print("Palabra separadas", list(word))
#     return cont_letter


# palabra()
import random
my_list = ["piedra", "papel", "tijera"]

def game():
    jugador1 = random.choice(my_list)
    jugador2 = random.choice(my_list)
    print(f"Jugador 1: {jugador1}, Jugador 2: {jugador2}")
    
    if jugador1 == jugador2:
        print("empate")
    elif jugador1 == "piedra" and jugador2=="tijera":
        print("jugador 1 gana")
    elif jugador1 == "papel" and jugador2=="piedra":
        print("jugador 1 gana")
    elif jugador1 == "tijera" and jugador2=="papel":
        print("jugador 1 gana")
    else:
        print("jugador2 gana")
        
game()
print(random.choice(my_list))


    
        