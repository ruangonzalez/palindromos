def is_palindrome(text: str) -> bool:
    """
    Função que verifica se o texto informado é um palíndromo!

    Regras:
    - Ignora letras maiúsculas e minúsculas.
    - Ignora espaços e caracteres especiais.
    - Aceita números também.
    """
    cleaned = "".join(char.lower() for char in text if char.isalnum())
    return cleaned == cleaned[::-1]


if __name__ == "__main__":
    word = input("👉 Digite uma palavra ou frase para verificar se é palíndromo: ")
    print(f"📏 O texto tem {len(word)} caracteres.")
    if is_palindrome(word):
        print(f"✅ '{word}' É um palíndromo!")
    else:
        print(f"❌ '{word}' Não é um palíndromo.")

