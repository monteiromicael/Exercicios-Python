import random

aleatorio = random.randrange(1, 100)
palpite = int(input('Chute um numero! '))


while True:
    if palpite > aleatorio:
        palpite = int(input('Chute um Valor menor! '))

    elif palpite < aleatorio:
        palpite = int(input('Chute um Valor Maior! '))

    elif palpite == aleatorio:
        print("Parabens Você Acertou!!")
        break