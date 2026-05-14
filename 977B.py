tam_arr = int(input())

letras = input()

two_grams = []

for i in range(tam_arr-1):
    particula = letras[i:i+2]
    two_grams.append(particula)

maior_valor = 0

for i in range(len(two_grams)):
    valor_atual = two_grams.count(two_grams[i])
    if valor_atual > maior_valor:
        maior_valor = valor_atual
        vencedor = two_grams[i]

print(vencedor)
