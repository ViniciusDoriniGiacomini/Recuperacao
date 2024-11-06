n = int(input("Digite o número limite: "))
mostrar_primos(n)

def mostrar_primos(n):
    for num in range(1, n + 1):
        if num > 1:
            for i in range(2, num):
                if num % i == 0:
                    break
            else:
                print(f"{num} é primo")
