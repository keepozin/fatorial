n = int(input("Digite um número: "))
if n > 0:
    fatorial = 1
    for item in range(1,n+1):
        fatorial = fatorial * item
print(fatorial)
    