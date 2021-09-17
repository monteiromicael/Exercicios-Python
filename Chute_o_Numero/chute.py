import PySimpleGUI as sg
import random

aleatorio = random.randrange(1, 100)
palpite = int(sg.popup_get_text("Chute um numero! "))

while True:
    if palpite > aleatorio:
        palpite = int(sg.popup_get_text("Chute um Valor menor! "))

    elif palpite < aleatorio:
        palpite = int(sg.popup_get_text("Chute um Valor maior! "))

    elif palpite == aleatorio:
        sg.popup("Parabens Você Acertou!!")
        break