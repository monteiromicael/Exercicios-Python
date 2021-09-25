import PySimpleGUI as sg


while True:
    sg.popup("")
    sg.popup('Robson está indo para a DragonBall Inc fazer uma entrevista para uma vaga de zelador, no caminho você se depara com um objeto caindo do céu.')


    pergunta1 = int(sg.popup_get_text('1 - Chegar Proximo para ver! \n2 - Ignorar para não se atrasar na entrevista!\n'))


    if pergunta1 == 1:
        while True:
            sg.popup('Chegando perto você vê um caderno preto escrito Death Note na capa! você fica curioso e guarda o caderno com você!')
            sg.popup('Quanto você ve no relógio, percebe que está atrasado para a entrevista, desesperado você olha ao seu redor procurando uma maneira de chegar a tempo')
            pergunta2 = int(sg.popup_get_text('1 - Pedir um taxi\n2 - Olhar para o céu\n3 - Correr'))
        
            if pergunta2 == 1:
                sg.popup('nice')
                pergunta3 = int(sg.popup_get_text('1 - deseja se matar?'))
            elif pergunta2 == 2:
                sg.popup('')
                pergunta3 = int(sg.popup_get_text('1 - deseja se matar?'))
            elif pergunta2 == 3:
                sg.popup('')
                pergunta3 = int(sg.popup_get_text('1 - deseja se matar?'))
            else:
                sg.popup('Coloque um numero valido!')


    elif pergunta1 == 2:
        print('2')
    else:
        print('Coloque um numero valido!')

