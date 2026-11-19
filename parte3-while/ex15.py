quantidade_positivos = 0
numero = int(input("Digite um numero (0 para parar): "))

while numero != 0:
    if numero > 0:
        quantidade_positivos += 1
    numero = int(input("Digite outro numero (0 para parar): "))

print("Quantidade de numeros positivos:", quantidade_positivos)
