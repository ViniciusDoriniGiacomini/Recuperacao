def piramide(n, crescente=True):
    for i in range(1, n + 1) if crescente else range(n, 0, -1):
        print(" ".join(str(a) for a in range(1, i + 1)))

numero = int(input("Digite um número: "))
piramide(numero)
