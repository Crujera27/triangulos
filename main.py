from functions.input import read_input
from functions.triangle import triangle_type
from functions.output import print_output

def main():
    cases = read_input()
    results = []

    for case in cases:
        result = triangle_type(case)
        results.append(result)

    print_output(results)

main()
