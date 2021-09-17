import player

player = player.Player("Robson", 23)

while True:
    print('Olá, agora você se chama Robson. Um jovem que está a procura de um novo emprego.')
    print('Robson está indo para a DragonBall Inc fazer uma entrevista para uma vaga de zelador, no caminho você se depara com um objeto caindo do céu.')
    print('\n')

    pergunta1 = int(input('1 - Chegar Proximo para ver! \n2 - Ignorar para não se atrasar na entrevista!\n'))


    if pergunta1 == 1:
        while True:
            print('Chegando perto você vê um caderno preto escrito Death Note na capa! você fica curioso e guarda o caderno com você!')
            print('')
            pergunta2 = int(input('1 - deseja se matar?'))
        
            if pergunta2 == 1:
                print('nice')
                pergunta3 = int(input('1 - deseja se matar?'))
            elif pergunta2 == 2:
                print('')
                pergunta3 = int(input('1 - deseja se matar?'))
            elif pergunta2 == 3:
                print('')
                pergunta3 = int(input('1 - deseja se matar?'))
            else:
                print('Coloque um numero valido!')


    elif pergunta1 == 2:
        print('2')
    else:
        print('Coloque um numero valido!')

