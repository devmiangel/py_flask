import os
os.system("cls")

#print(dir(list))

lista1 = [1,3,5,7,8,"nueve"]

#añadir un elemento al funal de la lista
lista1.append(2)
print(lista1)

#insertar elemento en indice especifico
lista1.insert(4,'cuatro')
print(lista1)

#añadir varios elementos al final de la lista
lista1.extend(["añade","varios","elementos","al","final"])
print(lista1)

#eliminar elementos de la lista
#elimina el primer elemento que se encuentra en coincidencioa 
lista1.remove('final')
print(lista1)

#borrado por indice y aparte retorna el elemento
#por defecto elimina el ultimo elemento de la lista
elemento_eliminado = lista1.pop()#se puede poner el indice
print(lista1)
print(elemento_eliminado)

#eliminar a lo hittler
del lista1[3]
print(lista1)

#limpiar lista
lista1.clear()
print(lista1)

#eliminar rango de elementos
lista1 = [1,3,5,7,8,"nueve"]
del lista1[:3]
print(lista1)

#ordenar listas pero modifica la lista original (no retorna nada)
lista1 = [1,22,47,45,8,39]
lista1.sort()
print(lista1)

#ordenar listas pero realiza una copia de la lista original y la ordena (Retorna el resultado)
lista1 = [1,22,47,45,8,39]
lista_ordenada = sorted(lista1)
print(lista_ordenada)

#orden de listas con string (solo minusculas)
lista1 = ["perro","gato","raton","raton","rata","caballo"]
animales = sorted(lista1)
print(animales)

#orden de listas con string (con mayusculas)
lista1 = ["perro","Gato","raton","Raton","rata","caballo"]
lista1.sort(key=str.lower)
print(lista1)

#conteo de cosas(si retorna valores)
lista1 = ["perro","gato","raton","raton","rata","caballo"]
conteo = lista1.count("raton")
print(conteo)

#hay elementos en listas??
lista1 = ["perro","gato","raton","raton","rata","caballo"]
print("hay un zoroo en la lista ","zorro" in lista1 )

