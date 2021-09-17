import random
import PySimpleGUI as sg

pergunta = sg.popup_get_text("Como posso te ajudar? ")
respostas = ['Com certeza, você deve fazer isso!',
            'Não sei, você que sabe',
            'Não faz isso Não!',
            'Acho que tá na hora certa!']

sg.popup(random.choice(respostas))
