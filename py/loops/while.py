#te permiten ejecutar un bloque de codigo mientras una condicion se cumpla
import os
os.system("cls")

num = 0

while num<12:
    print (num)
    num+=1

#la palabra brake es  para romper el bucle

while True:
    print ("hola")
    break

#continue, evita procesa una iteracion en concreto
print("-------------------------")
contador = 0 

while contador<= 10:
    contador+=1
    
    if contador % 2 == 0:
        continue
    
    print(contador)

print("-------------------------")

#se le puede meter un else al bucle cuando acaba
#en coso de que el bucle no se realize el else no se genera, esto pasa cuando al bucle lo interrumpe un break

contador = 0 

while contador<= 10:
    contador+=1
    
    if contador % 2 == 0:
        continue
    
    print(contador)
else:
    print("se acabo")
print("-------------------------")

#solitar informacion dentro de un bucle while

num = -1

while num <= 0:
    num = int(input("ingresa un numero: "))
    if num<0:
        print("el numero debe ser positivo")

print(f"El numero que ingresaste es el: {num}")
print("-------------------------")

#try catch que en python es try except

num = -1

while num <= 0:
    try:
        num = int(input("ingresa un numero: "))
        if num<0:
            print("el numero debe ser positivo")
    except:
        print("Se debe ingresar un numero crack")

print(f"El numero que ingresaste es el: {num}")
print("-------------------------")