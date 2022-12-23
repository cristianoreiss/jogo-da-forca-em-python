import os

palavra_secreta = input('Peça para um amigo escrever uma palavra e não tente olhar: ')
os.system('cls')  # comando para limpar o console

palavra_escondida = list(palavra_secreta)
index = []  # variável que vai armazenar o indices das letras da palavra secreta que são iguais ao chutes do jogador
chances = 6  # variável que contém as chances do jogador
letras_chutadas = []  # variável que vai guardar as letras chutas pelo jogador

for i in range(len(palavra_secreta)):  # laço para esconder a palavra secreta
    palavra_escondida[i] = '_'

while chances != 0:
    chute = input('\nDigite uma letra: ')
    if letras_chutadas.count(chute) != 0:  # condição que irá diminuir o número de chances se o jogador chutar uma palavra que já tenha chutado
        chances -= 1

    letras_chutadas.append(chute)

    if len(chute) > 1:
        print("Por favor, digite apenas uma letra por vez")
        continue

    index = [i for i, letra in enumerate(palavra_secreta) if letra == chute]

    for i in index:  # laço que irá percorrer a lista de indices e irá revelar as letras que o jogador acertou
        palavra_escondida[i] = chute

    index.clear()  # comando para apagar o conteúdo da lista parar poder armazenar indices da palavra secreta que correspondam ao novo possível chute certo do jogador
    palavra_maiuscula = (''.join(palavra_escondida)).upper()

    if palavra_secreta.count(chute) == 0:  # condicional que irá diminuir as chances do jogador se ele errar o chute ou se ele chutar um letra
        chances = chances - 1

    if palavra_maiuscula == palavra_secreta.upper():
        break
    else:
        print((''.join(palavra_escondida)).upper())
        if chances > 1:
            print(f'Você possui {chances} chances')
        else:
            print(f'Vôce possui {chances} chance')

if palavra_maiuscula == palavra_secreta.upper():
    print(f'\nA palavra secreta é {palavra_secreta.upper()}')
    print('\nVocê ganhou!!!')
else:
    print(f'\nA palavra secreta é {palavra_secreta.upper()}')
    print('Você perdeu :/')
