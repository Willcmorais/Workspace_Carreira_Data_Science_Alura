# Você recebeu uma demanda para gerar números de token para acessar o aplicativo de uma empresa. O token precisa ser par e variar de 1000 até 9998. Escreva um código que solicita à pessoa usuária o seu nome e exibe uma mensagem junto a esse token gerado aleatoriamente.
from random import randrange


def gerar_token():
    nome_user = input("Informe o seu nome: ")
    token_randomico = randrange(1000, 9999, 2)

    return f"Olá, {nome_user}.\nO seu token para acesso é o {token_randomico}.\nSeja bem-vindo(a)!"


def main():
    token_gerado = gerar_token()

    print(f"{token_gerado}")


if __name__ == "__main__":
    main()
