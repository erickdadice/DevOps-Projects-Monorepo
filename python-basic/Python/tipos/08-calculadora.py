n1 = input("Ingrese el primer número: ")
n2 = input("Ingrese el segundo número: ")
n1 = float(n1)
n2 = float(n2)
# Calculadora básica con operaciones aritméticas
# y el valor absoluto de los resultados
if n2 == 0:
    print("Error: No se puede dividir por cero.")
    exit()

mensaje = f"""
Para los numeros {n1} y {n2}:
La suma es: {n1 + n2}
La resta es: {n1 - n2}
La multiplicación es: {n1 * n2}
La división es: {n1 / n2}
El módulo es: {n1 % n2}
La potencia es: {n1 ** n2}
La división entera es: {n1 // n2}
El valor absoluto de la suma es: {abs(n1 + n2)}
El valor absoluto de la resta es: {abs(n1 - n2)}
El valor absoluto de la multiplicación es: {abs(n1 * n2)}
El valor absoluto de la división es: {abs(n1 / n2)}
El valor absoluto del módulo es: {abs(n1 % n2)}
"""
print(mensaje)
print("Operaciones realizadas correctamente.")
print("Gracias por usar la calculadora.")
