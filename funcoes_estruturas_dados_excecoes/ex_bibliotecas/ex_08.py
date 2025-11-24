# Para diversificar e atrair novos(as) clientes, uma lanchonete criou um item misterioso em seu cardápio chamado "salada de frutas surpresa". Neste item, são escolhidas aleatoriamente 3 frutas de uma lista de 12 para compor a salada de frutas da pessoa cliente. Crie o código que faça essa seleção aleatória de acordo com a lista abaixo:
from random import sample

frutas = [
    "Maçã",
    "Banana",
    "Uva",
    "Pêra",
    "Manga",
    "Coco",
    "Melancia",
    "Mamão",
    "Laranja",
    "Abacaxi",
    "Kiwi",
    "Ameixa",
]


def criar_salada_fruta_surpresa():
    frutas_escolhidas = sample(frutas, 3)

    return frutas_escolhidas


def main():
    salada_de_fruta = criar_salada_fruta_surpresa()

    print("A sua salada de fruta surpresa será feita com as frutas abaixo: ")

    for fruta in salada_de_fruta:
        print(f"- {fruta}")


if __name__ == "__main__":
    main()
