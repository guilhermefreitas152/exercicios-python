numero = int(input("Digite um numero inteiro nao negativo: "))

if numero < 0:
    print("Nao existe fatorial para numero negativo.")
else:
    fatorial = 1
    for valor in range(1, numero + 1):
        fatorial *= valor
    print("Fatorial:", fatorial)
