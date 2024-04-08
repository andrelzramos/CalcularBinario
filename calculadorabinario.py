
menu = """
[bd] - Binário para Decimal
[db] - Decimal para binário 
=> """

while True:
    print(menu)
    opcao = input()
    
    if opcao == "bd":
        binario = input("Digite um número binário: ")
        n = len(binario)

        decimal = 0
        for dig in binario:
            n -= 1
            decimal += int(dig)*2**n

        print(f'{decimal}[2] = {binario}[10]')
    
    elif opcao == "db":
        decimal = int(input("Digite o número decimal: "))
        temp = decimal

        binario = ''
        while decimal!= 0:
            binario = str(decimal%2) + binario
            decimal = decimal//2

        print(f'{temp}[2] = {decimal}[10]')
    else:
        print("Operação inválida!")
        



    
