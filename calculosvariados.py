n1 = int(input("Digite o primeiro número: "))
n2 = int(input("Digite o segundo número: "))
op = 0
while op != 5:
    print('''    [1] Somar
    [2] Multiplicar
    [3] Maior
    [4] Novos números
    [5] Sair do programa''')
    op = int(input("Digite a opção desejada: "))
    if op == 1:
        s = n1 + n2
        print("A soma de {} e {} é igual a {}".format(n1, n2, s))
    elif op == 2:
        x = n1 * n2
        print("{} vezes {} é igual a {}".format(n1, n2, x))
    elif op == 3:
        if n1 > n2:
            m = n1
            print("Entre {} e {}, o maior é {}".format(n1, n2, m))
        else:
            m = n2
            print("Entre {} e {}, o maior é {}".format(n1, n2, m))
    elif op == 4:
        print("Informe os números novamente: ")
        n1 = int(input("Digite o primeiro número: "))
        n2 = int(input("Digite o segundo número: "))
    elif op == 5:
        print("Finalizando...")

print("Fim do programa")
