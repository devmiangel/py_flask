###
# EJERCICIOS
# Usa siempre que puedas los métodos que has aprendido
###

# Ejercicio 1: Añadir y modificar elementos
# Crea una lista con los números del 1 al 5.
# Añade el número 6 al final usando append().
# Inserta el número 10 en la posición 2 usando insert().
# Modifica el primer elemento de la lista para que sea 0.

import os 
os.system("cls")

lista_numeros = [1,2,3,4,5]
lista_numeros.append(6)
lista_numeros.insert(2,10)
lista_numeros[0] = 0

print(lista_numeros)

print("----------------------")

# Ejercicio 2: Combinar y limpiar listas
# Crea dos listas:
# lista_a = [1, 2, 3]
# lista_b = [4, 5, 6, 1, 2]
# Extiende lista_a con lista_b usando extend().
# Elimina la primera aparición del número 1 en lista_a usando remove().
# Elimina el elemento en el índice 3 de lista_a usando pop(). Imprime el elemento eliminado.
# Limpia completamente lista_b usando clear().

lista_a = [1, 2, 3]
lista_b = [4, 5, 6, 1, 2]
lista_a.extend(lista_b)

lista_total = [1, 2, 3,4, 5, 6, 1, 2]
lista_total.remove(1)
print(lista_total)

elemento_eliminado = lista_total.pop(3)
print(elemento_eliminado)

lista_b.clear()
print(lista_b)

print(lista_a.extend(lista_b))

print("----------------------")

# Ejercicio 3: Slicing y eliminación con del
# Crea una lista con los números del 1 al 10.
# Utiliza slicing y del para eliminar los elementos desde el índice 2 hasta el 5 (sin incluir el 5).
# Imprime la lista resultante.

numeros_diez = [1,2,3,4,5,6,7,8,9,10]
del numeros_diez[2:4]
print(numeros_diez)

print("----------------------")

# Ejercicio 4: Ordenar y contar
# Crea una lista con los siguientes números: [5, 2, 8, 1, 9, 4, 2].
# Ordena la lista de forma ascendente usando sort().
# Cuenta cuántas veces aparece el número 2 en la lista usando count().
# Comprueba si el número 7 está en la lista usando in.


a_ordenar = [5, 2, 8, 1, 9, 4, 2]
a_ordenar.sort()
print(a_ordenar)

cant_dos = a_ordenar.count(2)
print(cant_dos)

valor_7 = 7 in a_ordenar
print(f"el valor 7 esta en lacadena {a_ordenar}? :{valor_7}")


print("----------------------")

# Ejercicio 5: Copia vs. Referencia
# Crea una lista llamada original con los números [1, 2, 3].
# Crea una copia de la lista original llamada copia_1 usando slicing.
# Crea otra copia llamada copia_2 usando copy().
# Crea una referencia a la lista original llamada referencia.
# Modifica el primer elemento de la lista referencia a 10.
# Imprime las cuatro listas (original, copia_1, copia_2, referencia) y observa los cambios.

original =  [1, 2, 3]
copia_1 = original[:]
print(copia_1)
copia_2 = original.copy()
print(copia_2)
referencia = original
referencia[0] = 10
print("lista original:", original)
print("lista copia_1:",copia_1 )
print("lista copia_2:",copia_2 )
print("lista referencia:", referencia )



print("----------------------")

# Ejercicio 6: Ordenar strings sin diferenciar mayúsculas y minúsculas.
# Crea una lista con las siguientes cadenas: ["Manzana", "pera", "BANANA", "naranja"].
# Ordena la lista sin diferenciar entre mayúsculas y minúsculas.

caden_may =  ["Manzana", "pera", "BANANA", "naranja"]
caden_may.sort(key=str.lower)
print(caden_may)