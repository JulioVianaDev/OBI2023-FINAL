texto=input()
letraAtual = texto[0]
repetidas = 0
for caracter in texto:
    if caracter == letraAtual:
        repetidas+=1
    else:
        print(f'{repetidas} {letraAtual}',end=" ")
        # atualizar a letra atual
        # contador voltar pra 1 
# printar o ultimo resultado