# rodar o tempo todo
    # perguntar nome
    # nome do enemy

    # loop infinito
        # eu jogo
        # multiplayer
            # se jogada for igual a a1
                # tela[0] = X
            # oponente joga
        # solo
            # jogadas geradas no random
        # olha se alguem venceu
            # conta ponto
    
    # pergunta se quer jogar de novo

from ast import Break

import os


def mostrar_tela():
    print("     1   2   3")
    print("A - [ ] [ ] [ ]\nB - [ ] [ ] [ ]\nC - [ ] [ ] [ ]")


def tela_do_jogo(nome_jogador, nome_oponente):
    tela = ["[ ]","[ ]","[ ]", "[ ]","[ ]","[ ]", "[ ]","[ ]","[ ]"]
    win = False
    while True:
        # for i in range(0,1):
        print("     1   2   3")
        print("A - "+tela[0],tela[1],tela[2])
        print("B - "+tela[3],tela[4],tela[5])
        print("C - "+tela[6],tela[7],tela[8])

        # testa se ganhou
        if tela[0] == "[X]" and tela[1] == "[X]" and tela[2] == "[X]":
            print("*"*20)
            print(f"parabéns {nome_jogador} você ganhou")
            print("*"*20)
            win = True

        if tela[3] == "[X]" and tela[4] == "[X]" and tela[5] == "[X]":
            print(f"parabéns {nome_jogador} você ganhou")
            win = True
        # para o game se ganhar
        if win == True:
            break

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


            

        # if win == True:
        #     break



# tela_do_jogo()



while True:
    nome_jogador = input("Digite seu nome\n")
    nome_oponente = input("Digite seu nome\n")
    os.system("cls")
    # mostrar_tela()
    # break
    print("Digite sua jogada, exemplo a1, b3, c2...")
    while True:
        tela_do_jogo(nome_jogador, nome_oponente)
        
        try:
            jogar_nov = int(input("[1] - jogar novamente\n[2] - sair\n"))
        except:
            print(f"[on red]Digite uma opção correta[/]")
            continue
        if jogar_nov == 1:
            break

        

 
