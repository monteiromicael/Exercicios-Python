import random

aleatorio = random.randrange(1, 100)
palpite = int(input('Chute um numero! '))


while True:
    if palpite > aleatorio:
        print('Chute um Valor menor!')
        palpite = int(input('Chute um numero! '))

    elif palpite < aleatorio:
        print("Chute um Valor Maior! ")
        palpite = int(input('Chute um numero! '))

    elif palpite == aleatorio:
        print("Parabens Você Acertou!!")
        break