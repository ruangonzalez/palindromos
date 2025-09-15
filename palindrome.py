def is_palindrome(text: str) -> bool:
    """
    Verifica se uma string é um palíndromo.
    Ignora maiúsculas/minúsculas e espaços.
    """
    cleaned = "".join(char.lower() for char in text if char.isalnum())
    return cleaned == cleaned[::-1]


if __name__ == "__main__":
    word = input("Digite uma palavra ou frase: ")
    if is_palindrome(word):
        print("✅ É um palíndromo!")
    else:
        print("❌ Não é um palíndromo.")
