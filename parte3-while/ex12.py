soma = 0
numero = int(input("Digite um numero (0 para parar): "))

while numero != 0:
    soma += numero
    numero = int(input("Digite outro numero (0 para parar): "))

print("Soma:", soma)
