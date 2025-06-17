animal = "  peRro Feliz  "
print(animal.upper())  # Convierte a mayúsculas
print(animal.lower())  # Convierte a minúsculas
print(animal.title())  # Convierte a formato de título
print(animal.strip().capitalize())  # Convierte la primera letra a mayúscula
print(animal.strip())  # Elimina espacios al inicio y al final
print(animal.replace("Feliz", "Triste"))  # Reemplaza una subcadena
print(animal.split())  # Divide la cadena en una lista de palabras
print(animal.lstrip())  # Elimina espacios al inicio
print(animal.rstrip())  # Elimina espacios al final
print(animal.find("Rr"))  # Encuentra la posición de una subcadena
print("Rr" in animal)  # Verifica si una subcadena está presente
# Verifica si la cadena comienza con una subcadena
print(animal.startswith("  peRro"))
# Verifica si la cadena termina con una subcadena
print(animal.endswith("Feliz  "))
print(animal.isalpha())  # Verifica si todos los caracteres son alfabéticos
print("Rr" not in animal)  # Verifica si una subcadena no está presente
print(animal.isnumeric())  # Verifica si todos los caracteres son numéricos
