def es_palindromo(frase):
    # Eliminar espacios y convertir a minúsculas
    frase = frase.replace(" ", "").lower()
    # Comparar la frase con su reverso
    return frase == frase[::-1]

# Ejemplo de uso
if __name__ == "__main__":
    texto = input("Introduce una palabra o frase: ")
    if es_palindromo(texto):
        print(f'"{texto}" es un palíndromo.')
    else:
        print(f'"{texto}" no es un palíndromo.')