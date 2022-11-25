import os

palavra_secreta = input('Peça para um amigo escrever uma palavra e não tente olhar: ')
os.system('cls')  # comando para limpar o console

palavra_escondida = list(palavra_secreta)
index = []  # variável que vai armazenar o indices das letras da palavra secreta que são iguais ao chutes do jogador
chances = 6  # variável que contém as chances do jogador

for i in range(len(palavra_secreta)):  # laço para esconder a palavra secreta
    palavra_escondida[i] = '_'

while chances != 0:
    letra = input('\nDigite uma letra: ')

    for i in range(len(palavra_secreta)):  # laço que vai armazenar no na variável 'index' os indices das letras da palavra secreta que são iguais ao chute do jogador
        if palavra_secreta[i] == letra:
            (index.append(i))

    for i in index:  # laço que irá percorrer a lista de indices e irá revelar as letras que o jogador acertou
        palavra_escondida[i] = letra

    index.clear()  # comando para apagar o conteúdo da lista parar poder armazenar indices da palavra secreta que correspondam ao novo possível chute certo do jogador
    palavra_maiuscula = (''.join(palavra_escondida)).upper()

    if palavra_secreta.count(letra) == 0:  # condicional que irá diminuir as chances do jogador se ele errar o chutepa
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
