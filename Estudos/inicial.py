a = int(input("informe um número maior que 10: "))

while a <= 10:
    print("Número menor do que o esperado!!!")
    a = int(input("Infome um número válido: "))
    continue

b = int(input("Agora informe um número multiplicador menor que 10: "))

while b >= 10:
    print("Número informado é maior que 10!!!")
    b = int(input("Informe um número válido"))
    continue

r = a * b

print(f"A multiplicação entre os números informados é: {r}")