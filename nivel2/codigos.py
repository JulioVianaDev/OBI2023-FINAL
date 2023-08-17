numero = int(input())
texto = input()
ultimaLetraChecada = texto[0]
repetiu = 0
for letraAtual in texto:
    if letraAtual == ultimaLetraChecada:
        repetiu +=1
    else:
        print(f'{repetiu} {ultimaLetraChecada}',end=" ")
        ultimaLetraChecada = letraAtual
        repetiu = 1
print(f'{repetiu} {ultimaLetraChecada}')