def format_crypto_quantity(value):
    # Converte o valor para uma string, preenche com zeros à direita para garantir 12 caracteres,
    # remove o ponto ou vírgula e retorna os últimos 11 caracteres.
    return str(value).ljust(12, '0').replace('.', '').replace(',', '')[-11:]


print(format_crypto_quantity(0.001))
print(format_crypto_quantity(0.01))
print(format_crypto_quantity(0.1))
