# Faça um programa para uma loja que vende grama para jardins. Essa loja trabalha com jardins circulares e o preço do metro quadrado da grama é de R$ 25,00. Peça à pessoa usuária o raio da área circular e devolva o valor em reais do quanto precisará pagar.
from math import pow, pi


def calcular_preco_metro_quadrado():
    VALOR_METRO_QUADRADO = 25

    raio_area = float(input("Informe o raio da área: "))
    area_circulo = pi * pow(raio_area, 2)
    preco_final = area_circulo * VALOR_METRO_QUADRADO

    return f"O valor total pela área de {area_circulo:.2f} metros quadrados é de R${preco_final:.2f}."


def main():
    preco = calcular_preco_metro_quadrado()
    print(preco)


if __name__ == "__main__":
    main()
