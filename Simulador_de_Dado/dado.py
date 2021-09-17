import random
import PySimpleGUI as sg

aleatorio = random.randrange(1, 7)


sg.popup("o resultado deu:", aleatorio)