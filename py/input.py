#funcion input

print("como te llamas")
nombre = input()

print(f"hola {nombre}")
age = input("cuantos años tienes:\n")
age=int(age)
print(f"En 20 años tendras {age+20}")

#para recuperar varios elmementos se usa la funcion split
country, city = input("En que pais y ciudad vives?\n").split()

print(f"vives en {country}, {city}")
