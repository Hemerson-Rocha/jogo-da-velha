# rodar o tempo todo
    # perguntar nome
    # nome do enemy

    # loop infinito
        # eu jogo
        # se jogada for igual a a1
            # tela[0] = X
        # oponente joga
        # olha se alguem venceu
            # conta ponto
    
    # pergunta se quer jogar de novo

def mostrar_tela():
    print("     1   2   3")
    print("A - [ ] [ ] [ ]\nB - [ ] [ ] [ ]\nC - [ ] [ ] [ ]")


def tela_do_jogo():
    tela = ["[ ]","[ ]","[ ]", "[ ]","[ ]","[ ]", "[ ]","[ ]","[ ]"]
    while True:
        for i in range(0,1):
            print("     1   2   3")
            print("A - "+tela[0],tela[1],tela[2])
            print("B - "+tela[3],tela[4],tela[5])
            print("C - "+tela[6],tela[7],tela[8])
            jogada = input("Sua jogada\n")
            jogada = jogada.strip().lower()
            print(jogada)
            if jogada == "a1":
                tela[0] = "[X]"
            elif jogada == "a2":
                tela[1] = "[X]"
            elif jogada == "a3":
                tela[2] = "[X]"
            
            elif jogada == "b1":
                tela[3] = "[X]"
            elif jogada == "b2":
                tela[4] = "[X]"
            elif jogada == "b3":
                tela[5] = "[X]"
            
            elif jogada == "c1":
                tela[6] = "[X]"
            elif jogada == "c2":
                tela[7] = "[X]"
            elif jogada == "c3":
                tela[8] = "[X]"
            else:
                print("Evite colocar espaços, exemplo a1, b3, c2..")



tela_do_jogo()



# while True:
#     # nome_jogador = input("Digite seu nome\n")
#     # nome_oponente = input("Digite seu nome\n")

#     # mostrar_tela()
#     # break
#     print("Digite sua jogada, exemplo a1, b3, c2...")
#     while True:
#         tela_do_jogo()
        

#     break
