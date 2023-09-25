def calcular_valor_maximo(operadores, operandos) -> float:
    # Operadores e sua função
    acoes = {"+": lambda a, b: a + b, 
            "-": lambda a, b: a - b,
            "*": lambda a, b: a * b,
            "/": lambda a, b: a / b,
            "%": lambda a, b: a % b}

    resultados = list(map(lambda op: acoes[op[0]](op[1][0], op[1][1]), zip(operadores, operandos)))
    maximo = max(resultados)
    return maximo

operadores = ['+','-','*','/','+']
operandos = [(3,6), (-7,4.9), (8,-8), (10,2), (8,4)]

resultado = calcular_valor_maximo(operadores, operandos)
print(resultado)
