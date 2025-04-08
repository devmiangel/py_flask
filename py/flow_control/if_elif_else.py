#es igual que toooodoooos los if

import os
os.system("cls")

edad = 19
if edad < 18:
    print("hay que crecer crack") 
elif 18<=edad<21:
    print("eres Mayor solo en latam")
else:
    print("ahora si estas grandecito")

#tambien se puede con and/or 
#se puede hacer negaciones, con el not (if not)
#condicionales anidados
#NO es necesario hacer una comparaciona

numero = 5 #este numero al no ser cer es True y entra en if
if numero:
    print("el numero no es cero")

numero = 0 
if numero:
    print ("aqui no va a entrar")

#pasa lo mismo con las cadenas de caracteres, si no hay nada se toma como false

#Es necesario que las condiciones seand verdaderas para entrar a estos if

numero = 3
numero_es_tres = numero ==3
if numero_es_tres:
    print("el numero es tres")

#Ternaria es una manera concisa de un if else
#[codigo si cumple condicion] if [condicion] else[codigo si no cumple la condicion]

edad = 17
mensaje = "es mayor de edad" if edad >=18 else "hay que crecer"
print(mensaje)