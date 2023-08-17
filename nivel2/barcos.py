ilhas, barcos = map(int,input().split())
listaPossibilidades = []
for i in range(barcos):
    inicio,fim,qtd = map(int,input().split())
    listaPossibilidades.append([inicio,fim,qtd ])

print(listaPossibilidades)