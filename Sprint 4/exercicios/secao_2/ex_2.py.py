def conta_vogais(texto: str) -> int:
    vogais = 'aeiouAEIOU'
    vogais_encontradas = list(filter(lambda letra: letra in vogais, texto))
    return len(vogais_encontradas)