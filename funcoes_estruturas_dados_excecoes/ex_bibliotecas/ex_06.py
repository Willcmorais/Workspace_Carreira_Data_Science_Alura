# Um programa deve ser escrito para sortear uma pessoa seguidora de uma rede social para ganhar um prêmio. A lista de participantes é numerada e devemos escolher aleatoriamente um número de acordo com a quantidade de participantes. Peça à pessoa usuária para fornecer o número de participantes do sorteio e devolva para ela o número sorteado.

from random import randrange


def sortear():
    lista_participantes = int(
        input("Informe a quantidade de pessoas que participarão do sorteio: ")
    )

    pessoa_sorteada = randrange(1, lista_participantes + 1)

    return pessoa_sorteada


def main():
    sorteio = sortear()
    print(f"O número sorteado foi o {sorteio}!")


if __name__ == "__main__":
    main()
