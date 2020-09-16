# PRACTICA I: VARIABLES, TIPOS DE DATOS, EXPRESIONES Y CONDICIONALES (By "J3.py"): 

# 1- Escriba en pantalla el tipo de dato que retorna la expresión 4 < 2

print(4 < 2)
print()

# 2- Almacene en una variable el nombre de una persona y al final muestre en la consola el mensaje: “Bienvenido [nombrePersona]”

name = input("Add name ")
print("Bienvenido " + name)

# 3- Evalúe si un número es par o impar y muestre en la consola el mensaje.

num = int(input("Enter a number: "))
if (num % 2) == 0:
   print("{0} is Even".format(num))
else:
   print("{0} is Odd".format(num))

# 4- Almacene dos números y evalúe si el primero es mayor que el segundo. El resultado debe verse en la consola.

num1 = input("number ")
num2 = input("number ")
if num1 > num2:
    print(num1 + "is greater than " + num2 )

# 5- Convierta dólares a pesos.

USD = input("Amount in Dollars ")
DOP = 58.55
Exange = (USD * DOP)
print("Amount in Pesos " + (Exange))

# 6- Convierta grados celsius a Fahrenheit

celciusTemperature = float( input( "Inseter la temperature en Celcius " ) )

fahrenheitTemperature = ( ( 9 / 5 ) * celciusTemperature ) + 32
print( fahrenheitTemperature )

# 7- Almacene cuatro notas 90, 95, 77, 92 y las promedie. Al final debe decir su calificación en letras A, B,C,D, E ó F.

nota1 = 90 
nota2 = 95
nota3 = 77
nota4 = 92
promedio = float(nota1 + nota2 + nota3 + nota4)
if promedio >= 90:
    print("A")
elif promedio >= 80 & promedio <= 89:
    print("B")
elif promedio >= 70 & promedio <= 79:
    print("C")
elif promedio >= 60 & promedio <= 69:
    print("D")
elif promedio <= 59:
    print("F")
    
# 8- Que almacene monto, cantidad de cuotas, y porcentaje de interés anual de un préstamo y calcule la cuota mensual. (Amortizar mediante el sistema francés)

