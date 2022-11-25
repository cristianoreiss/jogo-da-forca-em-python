import os

palavra_secreta = input('Peça para um amigo escrever uma palavra e não tente olhar: ')
os.system('cls')

palavra_escondida = list(palavra_secreta)
index = []
chances = 6

for i in range(len(palavra_secreta)):
    palavra_escondida[i] = '_'

while chances != 0:
    letra = input('\nDigite uma letra: ')

    for i in range(len(palavra_secreta)):
        if palavra_secreta[i] == letra:
            (index.append(i))

    for i in index:
        palavra_escondida[i] = letra

    index.clear()
    palavra_maiuscula = (''.join(palavra_escondida)).upper()

    if palavra_secreta.count(letra) == 0:
        chances = chances - 1

    if palavra_maiuscula == palavra_secreta.upper():
        break
    else:
        print((''.join(palavra_escondida)).upper())

if palavra_maiuscula == palavra_secreta.upper():
    print(f'\nA palavra secreta é {palavra_secreta.upper()}')
    print('\nVocê ganhou!!!')
else:
    print(f'\nA palavra secreta é {palavra_secreta.upper()}')
    print('Você perdeu :/')