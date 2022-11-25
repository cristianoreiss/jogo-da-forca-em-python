palavra_secreta = input('Peça para um amigo escrever uma palavra e não tente olhar: ')
letra = input('Digite uma letra: ')
palavra_escondida = list(palavra_secreta)
index = []

for i in range(len(palavra_secreta)):
    palavra_escondida[i] = '_'
print(palavra_escondida)


for i in range(len(palavra_secreta)):
    if palavra_secreta[i] == letra:
        (index.append(i))
        print(index)

for i in index:
    palavra_escondida[i] = letra
    print(palavra_escondida)
