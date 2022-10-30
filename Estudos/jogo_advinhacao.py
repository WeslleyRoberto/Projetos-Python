from random import randint
import time

print('Seja bem vindo ao desafio de advinhação!\n')
time.sleep(2)
print('O objetivo é advinhar um número entre 1 e 100 esolhido aleatório pelo PC.\n')
time.sleep(3)
print('Você terá um número de chances de acordo com a dificuldade escolhida:\n')
time.sleep(3)
print('1 - Fácil (10 tentativas)\n'
      '2 - Médio (5 tentativas)\n'
      '3 - Difícil (3 tentativas)\n')
time.sleep(3)
print('Preparado???\n')
time.sleep(1),
print('Vamos começar...')
time.sleep(2)

n_secreto = randint(1, 100)
chances = []
palpite = []
tentativas = 0
recomecar = 'sim'
chutes = []

while recomecar == 'sim':
    chutes.clear()

    try:
        nivel = int(input('\nEscolha a dificudade: '))
    except ValueError:
        print('Não entendi. Informe uma dificuldade válida: ')
        continue

    while nivel < 1 or nivel > 3:
        try:
            print('\nNivel de dificuldade inválido!')
            nivel = int(input('Informe uma dificuldade válida: '))
        except ValueError:
            print('Não entendi. Informe uma dificuldade válida: ')
            continue

    if nivel == 1:
        chances = 10
    elif nivel == 2:
        chances = 5
    else:
        chances = 3

    print(f'\nÓtimo!!! você terá {chances} chances.\n')

    for rodada in range(1, chances + 1):
        try:
            palpite = int(input(f'Advinhe o número (tentativa {rodada} de {chances}): '))
            tentativas += 1
            chutes.append(palpite)
        except ValueError:
            continue

        if palpite < n_secreto:
            print('O número secreto é maior.')
        elif palpite > n_secreto:
            print('O número secreto é menor.')
        else:
            print(f'\nParabéns!!! Você acertou em {tentativas} tentativas!!!')
            print(f'Os seus palpites foram: {chutes}')
            break

    print('\nFIM DO JOGO!!!')

    if tentativas == chances:
        print(f'O número secreto era {n_secreto}')
        print(f'Os seus palpites sem sucesso foram: {chutes}')

    recomecar = input('\nDeseja jogar novamente? (sim/não): ')

    while recomecar == '':
        print('Não entendi.')
        recomecar = input('\nDeseja jogar novamente? (sim/não): ')
        continue
    if recomecar == 'não':
        print('Obrigado por jogar!!!')