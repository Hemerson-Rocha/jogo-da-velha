# rodar o tempo todo
    # perguntar nome
    # nome do enemy

    # loop infinito
        # eu jogo
        # oponente joga
        # olha se alguem venceu
            # conta ponto
    
    # pergunta se quer jogar de novo

def mostrar_tela():
    print("[ ] [ ] [ ]\n[ ] [ ] [ ]\n[ ] [ ] [ ]")


def tela_do_jogo():
    tela = ["[ ]","[ ]","[ ]", "[ ]","[ ]","[ ]", "[ ]","[ ]","[ ]"]
    for i in range(0,1):
        print(tela[0],tela[1],tela[2])
        print(tela[3],tela[4],tela[5])
        print(tela[6],tela[7],tela[8])

        
mostrar_tela()


# while True:
#     nome_jogador = input("Digite seu nome\n")
#     nome_oponente = input("Digite seu nome\n")

#     while True:
#         tela_do_jogo()
