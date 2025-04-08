###
# exercises.py
# Ejercicios para practicar los conceptos aprendidos en las lecciones.
###

from os import system
if system("clear") != 0: system("cls")

print("\nEjercicio 1: Imprimir mensajes")
print("Escribe un programa que imprima tu nombre y tu ciudad en líneas separadas.")

### Completa aquí

print("Mi nombre es tal")
print("y vio en cual")

print("--------------")

print("\nEjercicio 2: Muestra los tipos de datos de las siguientes variables:")
print("Usa el comando 'type()' para determinar el tipo de datos de cada variable.")
a = [15,3.14159,"Hola mundo",True,None,]

for valores in a:
    print(type(valores))

### Completa aquí

print("--------------")

print("\nEjercicio 3: Casting de tipos")
print("Convierte la cadena \"12345\" a un entero y luego a un float.")
print("Convierte el float 3.99 a un entero. ¿Qué ocurre?")

cadena = "12345"
cadena=int(cadena)
print(type(cadena))
cadena=float(cadena)
print(type(cadena))

### Completa aquí

print("--------------")

print("\nEjercicio 4: Variables")
print("Crea variables para tu nombre, edad y altura.")
print("Usa f-strings para imprimir una presentación.")

name = "tal"
age = "tantos"
heigh = "esto"

print(f"Hola me llamo {name}, tengo {age} años y mido {heigh}")

### Completa aquí

print("--------------")

print("\nEjercicio 5: Números")
print("1. Crea una variable con el número PI (sin asignar una variable)")
print("2. Redondea el número con round()")
print("3. Haz la división entera entre el número que te salió y el número 2")
print("4. El resultado debería ser 1")

resultado = (int(round(3.1416)/2))
print(f"el valor de pi aproximado es {round(3.1416)}")
print(f"ahora dividido dos y pasado a int es: {resultado}")
