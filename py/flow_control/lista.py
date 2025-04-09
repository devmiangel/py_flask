#lista es tener un conjunto de elementos bajo un mismo nombre
import os
os.system("cls")

lista = [1,"gol",True,2.3,5,"otro gol"]
lista_numeros = [0,1,2,3,4,5,6,7,8,9,10]
lista_de_listas =[[1,2],[2,3]]
matrix =  [[1,2],[2,3],[4,6]]

#acceso a elementos por indice
print(lista[0])
print(lista[-1])#accede al ultimo elemento

print (matrix [1][0])

#Slicing (rebanando) de listas
#deja ciertos elementos de la lista en un array especifico

nueva_lista = lista[1:5] #ciertos elementos de la lista
lista_inicial= lista[:3] #Lista de los primeros tres elementos
lista_final = lista[4:] #lista de los ultimos elementos 
copia_lista = lista[:] #hace una copia de la lista completa

print(nueva_lista)

#lista[dede:hasta:paso]
#el paso es de uno en uno, puede ser de dos en dos etc
lista_par = lista_numeros[::2] 
print(lista_par)

lista_invertida = lista_numeros[::-1]
print(lista_invertida)

#modificar lista - de tooooodaaa la vida
lista_numeros[0] = 23

#añadir elementos
#forma 1
lista_numeros =lista_numeros + [11,12,13]
print(lista_numeros)

#forma2 - mejor y mas eficiente
lista_numeros += [14,15,16]
print(lista_numeros)

#recuperar longitud de una lista
print(len(lista_numeros))
