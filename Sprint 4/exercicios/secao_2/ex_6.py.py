def maiores_que_media(conteudo: dict) -> list:
    # Calcular a média dos preços
    media = sum(conteudo.values()) / len(conteudo)

    # Filtrar os produtos com preço acima da média e ordenar por preço (ordem crescente)
    produtos_acima_media = [(produto, preco) for produto, preco in conteudo.items() if preco > media]
    produtos_acima_media.sort(key=lambda x: x[1])

    return produtos_acima_media


