# PRUEBA 2 - EJERCICIO 1: SISTEMA DE MEDICAMENTOS Y DESPACHO

print("\n--- CÁLCULO DE PACK MEDICAMENTOS Y DESPACHO ---")

# Valores base establecidos por el enunciado
COSTO_MEDICAMENTOS = 60000
COSTO_DESPACHO = 8000

# 1. Validación de la edad mediante ciclo while y try/except
edad_valida = False
while not edad_valida:
    try:
        edad = int(input("Ingrese su edad: "))
        if edad > 0:
            edad_valida = True
        else:
            print("Error: Debe ingresar un numero entero positivo.")
    except_ValueError
        print("Error: Debe ingresar un número entero válido.")
        
 
# 2. Validación y normalización del tramo ( Debe ser A, B, C o D)
tramo_valido = False
while tramo_valido == False:
    tramo = input("Ingrese su tramo ( A, B, C o D): ")
    tramo = tramo.upper().strip() # Convierte mayúsculas y quita espacios vacios

    if tramo == "A" or tramo == "B" or tramo == "C" or tramo == "D":
        tramo_valido = True
    else:
        print("Error: Tramo invalido, Ingrese solo A, B, C o D.")


# 3. Determinación del descuento para Medicamentos segúnlas tablas
porcentaje_med = 0.0

if edad <= 30:
    if tramo == "A" or tramo =="B":
        porcentaje_med =0.18
    elif tramo == "C" or tramo == "D":
        porcentaje_med = 0.12
elif edad >= 31 and edad <= 60:
        if tramo == "A" or tramo == "B":
            porcentaje_med = 0.12
        else:
            porcentaje_med = 0.08 


# 4. Determinación del descuento para el Despacho
            porcentaje_despacho = 0.0 # Inicialización  de la variable

if tramo == "A" or tramo == "B":

            porcentaje_despacho += 0.10  # 10% por pertenecer al tramo A o B

if edad >= 55:

        porcentaje_despacho += 0.05 # 5% adicional si tiene 55 años o más


# 5. Cálculos económicos finales aplicando los porcentajes correspondientes  
desc_medicamentos = COSTO_MEDICAMENTOS * porcentaje_med
final_medicamentos = COSTO_MEDICAMENTOS - desc_medicamentos

desc_despacho = COSTO_DESPACHO * porcentaje_despacho
final_despacho = COSTO_DESPACHO - desc_despacho 


# 6. Mostrar salidas 
print(f"El valor de medicamentos es: {int(final_medicamentos)}")
print(f"El  valor del despacho es: {int(final_despacho)}")
