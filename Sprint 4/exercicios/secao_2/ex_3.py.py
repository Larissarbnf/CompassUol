from functools import reduce

def ajustar_o_lancamento (lancamento):
    valor = (lancamento[0] if lancamento[1] == 'C' else - lancamento[0])
    return valor

def calcula_saldo(lancamentos) -> float:
    ajustados = map(ajustar_o_lancamento, lancamentos)

    # Calcular o saldo final com reduce
    saldo_final = reduce(lambda a, b: a + b, ajustados, 0)

    return saldo_final

lancamentos = [
    (200,'D'),
    (300,'C'),
    (100,'C')
]

resultado = calcula_saldo(lancamentos)
print(resultado)

