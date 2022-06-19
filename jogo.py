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
from rich import print
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

        # validação vertical
        if tela[0] == "[X]" and tela[1] == "[X]" and tela[2] == "[X]":
            print("*"*20)
            print(f"parabéns {nome_jogador} você ganhou")
            print("*"*20)
            win = True

        elif tela[3] == "[X]" and tela[4] == "[X]" and tela[5] == "[X]":
            print("*"*20)
            print(f"parabéns {nome_jogador} você ganhou")
            print("*"*20)            
            win = True

        elif tela[6] == "[X]" and tela[7] == "[X]" and tela[8] == "[X]":
            print("*"*20)
            print(f"parabéns {nome_jogador} você ganhou")
            print("*"*20)            
            win = True





        # validação vertical
        elif tela[0] == "[X]" and tela[3] == "[X]" and tela[6] == "[X]":
            print("*"*20)
            print(f"parabéns {nome_jogador} você ganhou")
            print("[on blue]erro aqui[/]")
            print("*"*20)            
            win = True

        elif tela[1] == "[X]" and tela[4] == "[X]" and tela[7] == "[X]":
            print("*"*20)
            print(f"parabéns {nome_jogador} você ganhou")
            print("[on green]erro aqui[/]")
            print("*"*20)            
            win = True

        elif tela[2] == "[X]" and tela[5] == "[X]" and tela[8] == "[X]":
            print("*"*20)
            print(f"parabéns {nome_jogador} você ganhou")
            print("[on red]erro aqui[/]")
            print("*"*20)            
            win = True







        elif tela[0] == "[X]" and tela[4] == "[X]" and tela[8] == "[X]":
            print("*"*20)
            print(f"parabéns {nome_jogador} você ganhou")
            print("*"*20)            
            win = True

        elif tela[2] == "[X]" and tela[4] == "[X]" and tela[6] == "[X]":
            print("*"*20)
            print(f"parabéns {nome_jogador} você ganhou")
            print("[on red]erro aqui[/]")
            print("*"*20)            
            win = True

        # elif tela[2] == "[X]" and tela[4] == "[X]" and tela[6] == "[X]":
        #     print("*"*20)
        #     print(f"parabéns {nome_jogador} você ganhou")
        #     print("*"*20)            
        #     win = True

        


        # para o game se ganhar
        if win == True:
            break

        jogada = input("Sua jogada\n")
        os.system("cls")
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


            

        







while True:
    nome_jogador = input("Digite seu nome\n")
    nome_oponente = input("Digite seu nome\n")
    os.system("cls")

    print("Digite sua jogada, exemplo a1, b3, c2...")
    while True:
        tela_do_jogo(nome_jogador, nome_oponente)

        while True:    
            try:
                jogar_nov = int(input("[1] - jogar novamente\n[2] - sair\n"))
                if jogar_nov == 1 or jogar_nov == 2:
                    break
                else:
                    os.system("cls")
                    print(f"[on red]Digite uma opção válida[/]")
                    continue
                    
            except:
                os.system("cls")
                print(f"[on red]Não digite letras[/]")


            
        if jogar_nov == 1:
            break
        if jogar_nov == 2:
            break
    
    if jogar_nov == 2:
        break

        

 
