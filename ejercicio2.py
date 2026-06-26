# PRUEBA 2 # EJERCICIO 2: JUEGO DE ADIVINANAZA PAR

from random import randint

print("\n---INICIANDO EJERCICIO 2: JUEGO DE NÚMEROS ---")

# 1. Ingreso y validación del rango
while True:
     try:
          num1 = int(input("Ingrese límite inferior: "))
          num2 = int(input("Ingrese límite superior: "))
          if num1 < num2:
               break
          else:
               print("Error: El primer valor debe ser menor que el segundo.")
     except ValueError:
               print("Error: Ingrese números enteros válidos.")

# 2. Generar número aleatorio
numero_secreto = randint(num1, num2)

# 3. Ajustar para asegurar que el número final sea PAR
if numero_secreto % 2 != 0: # Si es impar
     if(numero_secreto + 1) <= num2:
        numero_secreto = numero_secreto + 1
     else:
          numero_secreto = numero_secreto -1 

# Guardamos las respuestas para la pista del intento 2
intento_1 = None
intento_2 = None
adivino = False

# 4. Desarrollo de los 3 Intentos

# ----- INTENTO 1 -----
intento_1 = int(input("Intente adivinar: "))

if intento_1 == numero_secreto:
     print("Felicitaciones, adivinó en el primer intento.")
     adivino = True
else:
     if intento_1 < numero_secreto:
          print("El número es mayor.")
     else:
          print("El número es menor.")

# ----- INTENTO 2 -----
if not adivino:
     intento_2 = int(input("Intente de nuevo: "))

     if intento_2 == numero_secreto:
          print("Felicitaciones, adivinó en su segundo intento.")
          adivino = True
     else:
          if intento_2 < numero_secreto:
               print("El número es mayor.")
          else:
               print("El número es menor.")

print("Te dare una pista:")
# Calcular cuál intento estuvo más cerca
distancia_1 = abs(numero_secreto - intento_1)
distancia_2 = abs(numero_secreto - intento_2)

if distancia_1 < distancia_2:
     print(f"El número que buscas está más cerca de {intento_1} que de {intento_2}")
elif distancia_2 < distancia_1:
     print(f"El número que buscas esta más cerca de {intento_2}que de{intento_1}")
        else:
     print(f"Ambos intentos ({intento_1} y {intento_2}) están a la misma distancia.")
# ----- INTENTO 3 -----
if not adivino:
     intento_3 = int(input("Intente la última vez: "))

     if intento_3 == numero_secreto:
          print("Felicitaciones, pudiste adivinar.")
          adivino: True
     else:
          print("Perdiste.")
          print(f"El n+umero era:{numero_secreto}")
