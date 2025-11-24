# Você recebeu um desafio de calcular a raiz quadrada de uma lista de números, identificando quais resultaram em um número inteiro. A lista é a seguinte:
from math import sqrt

numeros = [2, 8, 15, 23, 91, 112, 256, 81, 7, 25]


def tirar_raiz_quadrada():
    raizes = {}
    for numero in numeros:
        raiz_quadrada = sqrt(numero)
        if raiz_quadrada // 1 == raiz_quadrada:
            raizes[numero] = raiz_quadrada

    return raizes


def main():
    raizes_quadradas = tirar_raiz_quadrada()
    print("Números que possuem raízes quadradas inteiras: ")

    for valor, raiz in raizes_quadradas.items():
        print(f"Raiz quadradada de {valor} é igual à {raiz}")


if __name__ == "__main__":
    main()
