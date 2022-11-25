palavra_secreta = input('Peça para um amigo escrever uma palavra e não tente olhar: ')

palavra_escondida = list(palavra_secreta)
index = []
chances = 6

for i in range(len(palavra_secreta)):
    palavra_escondida[i] = '_'

while chances != 0:
    letra = input('Digite uma letra: ')


    for i in range(len(palavra_secreta)):
        if palavra_secreta[i] == letra:
            (index.append(i))

    for i in index:
        palavra_escondida[i] = letra

    index.clear()
    chances = chances - 1
    print(''.join(palavra_escondida))
else:
    print(''.join(palavra_escondida))

