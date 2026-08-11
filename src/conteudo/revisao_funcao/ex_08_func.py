def media_pares(n):
    quantidade = n // 2
    if quantidade == 0:
        return 0

    return quantidade + 1

print(media_pares(10))