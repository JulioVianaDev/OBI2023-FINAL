N = int(input())
sequence = [int(input()) for _ in range(N)]
maoirDistancia = 0
listaAtual = set()
index = 0
for num in sequence:
    while num in listaAtual:
        listaAtual.remove(sequence[index])
        index += 1
    listaAtual.add(num)
    maoirDistancia = max(maoirDistancia, len(listaAtual))

print(maoirDistancia)