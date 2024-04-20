import re

def read_input():
    num_cases = int(input("Ingrese el número de pruebas: "))
    cases = []

    for case_num in range(1, num_cases + 1):
        print(f"Caso de prueba #{case_num}:")
        sides_input = input("Ingrese las longitudes de los tres lados separadas por espacios: ")
        
        sides = re.split(r'\s+', sides_input.strip())

        try:
            sides = list(map(int, sides))
            if len(sides) != 3:
                raise ValueError("Por favor, pon exactamente tres enteros separados por espacios.")
            if any(side <= 0 for side in sides):
                raise ValueError("Todas las longitudes de los lados deben ser enteros positivos.")
        except ValueError as e:
            print(f"Entrada inválida: {e}. Por favor, inténtelo de nuevo.")
            return read_input()

        cases.append(sides)

    return cases

