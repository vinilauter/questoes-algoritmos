def merge_sort(arr):
    if len(arr) > 1:
        meio = len(arr) // 2
        esquerda = arr[:meio]
        direita = arr[meio:]

        merge_sort(esquerda)
        merge_sort(direita)

        i = j = k = 0
        while i < len(esquerda) and j < len(direita):
            if esquerda[i] < direita[j]:
                arr[k] = esquerda[i]
                i += 1
            else:
                arr[k] = direita[j]
                j += 1
            k += 1

        if i < len(esquerda):
            arr[k:] = esquerda[i:]
        if j < len(direita):
            arr[k:] = direita[j:]
    return arr


# o input dá o número de caiaques duplos total de pessoas é 2 * n.
n = int(input())
total_pessoas = 2 * n
    
pesos = [int(x) for x in input().split()]
    
merge_sort(pesos)
    
# inicia a resposta com infinito
menor_instabilidade = float('inf')
    
for i in range(total_pessoas):
        
    
    for j in range(i + 1, total_pessoas):
            
        sobreviventes = []
            
        for k in range(total_pessoas):
            if k != i and k != j:
                sobreviventes.append(pesos[k])
            
            
        instabilidade_simulacao = 0
            
        for k in range(0, len(sobreviventes), 2):
                
            diferenca = sobreviventes[k+1] - sobreviventes[k]
            instabilidade_simulacao += diferenca
            
            
        if instabilidade_simulacao < menor_instabilidade:
            menor_instabilidade = instabilidade_simulacao

print(menor_instabilidade)
