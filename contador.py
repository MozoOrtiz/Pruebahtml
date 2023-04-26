numero_negativo = -100
positivo = numero_negativo * -1
print(
    f"El número negativo es {numero_negativo} y convertido a positivo es {positivo}")
# Con la función "abs" de valor absoluto también es posible
numero_negativo = -100
positivo = abs(numero_negativo)
print(
    f"El número negativo es {numero_negativo} y convertido a positivo con abs es {positivo}")
# Otra prueba
numero_usuario = float(input("Ingresa un número: "))
# Convertir solo si es negativo
if numero_usuario < 0:
    numero_usuario *= -1

print(f"El número que ingresaste es {numero_usuario} de manera positiva")