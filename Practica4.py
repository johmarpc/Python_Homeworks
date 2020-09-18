# Practica IV: Python

# 1- Modele tres entidades del mundo real, colocar por lo menos 3 características distintivas.

Invoice = ("Costos ", "Ingresos ", "deudas")
Account = ("Acceso ", "Informacion ", "Conatabilidad ")
Customers = ("Persona ", "Comapañia ", "Organizacion ")

# 2- Crear una clase llamada Estudiante con un campo llamado promedio, el cual  solo podrá ser accedido mediante un metodo. 
#    El valor del promedio no puede estar por encima de 100 que es la nota máxima.

class Student:
    def __init__(self, promedio):
        self.promedio = promedio
    promedio > 100

# 3- Hacer una clase llamada Aritmética, que contenga métodos para cada una de las operaciones aritméticas básicas.

class Aritmetica:
    def Math(self, Add, Sub, Mul):
        pass
    
    def self.add:
         1 + 1
    
    def self.Sub:
         1 - 1

    def self.Mul:
        1 * 1


# 4- Cree una clase llamada Personaje con los métodos de instancia MoverArriba,  MoverAbajo, MoverDerecha y MoverIzquierda. 
#    Cree una clase llamada Mario y  otra clase llamada Koopa que herede las funcionalidades de la clase Personaje.

class Personaje:
    moveUp
    moveDown
    moveLeft
    moveRight

class Mario(Personaje):
    Personaje.moveUp
    Personaje.moveDown
    Personaje.moveLeft
    Personaje.moveRight

class Koopa(Personaje): #Bowser
    Personaje.moveUp
    Personaje.moveDown
    Personaje.moveLeft
    Personaje.moveRight

# 5- Cree una clase Carro, con un campo llamado _cantidadCombustible y un  método que se llame Encender el cual en base 
#    a la gasolina disponible  mostrara si el carro pudo o no avanzar. Cada vez que el método se ejecute, 
#    deberá restarse 1 a la gasolina disponible. La cantidad de gasolina debe  establecerse al momento de instanciar 
#    un objeto de del tipo de la clase.

class Car:
    def __init__(self, galones):
        self.cantidadCombustible = galones

    def Encender(self):
        if self.encedido == False and self.cantidadCombustible > 0:
            self.encedido = True
            print("Start Car")
    
    def Apagar(self):
        if self.encendido:
            self.encedido = False

    def Acelerar(self):
        if self.encedido:
            self.cantidadCombustible = 1

    def Frenar(self):
        print("Stop")


