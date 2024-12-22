#%%
# Projeto Jogo da velha
# Curso Python starter - ASIMOV
# 10.12.2024
import random
import time
import os

class JogoDaVelha1x1:
    
    tabuleiro = {'7':' ','8':' ','9':' ',
                 '4':' ','5':' ','6':' ',
                 '1':' ','2':' ','3':' '}
    turno = None
    
    def __init__(self, jogador_inicial="X"):
        self.tabuleiro = {'7':' ','8':' ','9':' ',
                 '4':' ','5':' ','6':' ',
                 '1':' ','2':' ','3':' '}
        self.turno = jogador_inicial
    
    def exibirtabuleiro(self):
        print("┌───┬───┬───┐")
        print(f"| {self.tabuleiro['7']} | {self.tabuleiro['8']} | {self.tabuleiro['9']} |")
        print("├───┼───┼───┤")
        print(f"| {self.tabuleiro['4']} | {self.tabuleiro['5']} | {self.tabuleiro['6']} |")
        print("├───┼───┼───┤")
        print(f"| {self.tabuleiro['1']} | {self.tabuleiro['2']} | {self.tabuleiro['3']} |")
        print("└───┴───┴───┘")

    def verificarjogada(self, jogada):
        if jogada in self.tabuleiro.keys():
            if self.tabuleiro[jogada] == " ":
                return True
        return False

    def verificartabuleiro(self):
        # Verificação em 3 verticais
        if self.tabuleiro['7'] == self.tabuleiro['4'] == self.tabuleiro['1'] != " ":
            return self.tabuleiro['7']
        if self.tabuleiro['8'] == self.tabuleiro['5'] == self.tabuleiro['2'] != " ":
            return self.tabuleiro['8']
        if self.tabuleiro['9'] == self.tabuleiro['6'] == self.tabuleiro['3'] != " ":
            return self.tabuleiro['9']
        
        # Verificações das 3 horizontais
        if self.tabuleiro['7'] == self.tabuleiro['8'] == self.tabuleiro['9'] != " ":
            return self.tabuleiro['7']
        if self.tabuleiro['4'] == self.tabuleiro['5'] == self.tabuleiro['6'] != " ":
            return self.tabuleiro['4']
        if self.tabuleiro['1'] == self.tabuleiro['2'] == self.tabuleiro['3'] != " ":
            return self.tabuleiro['1']
        
        # Verificações das 2 diagonais
        elif self.tabuleiro['7'] == self.tabuleiro['5'] == self.tabuleiro['3'] != ' ':
          return self.tabuleiro['7']
        elif self.tabuleiro['1'] == self.tabuleiro['5'] == self.tabuleiro['9'] != ' ':
          return self.tabuleiro['1']

        # Verificando empate
        if [*self.tabuleiro.values()].count(' ') == 0:
            return "empate"
        else:
            return [*self.tabuleiro.values()].count(' ')

    def jogar(self):
        while True:
            os.system('cls')
            self.exibirtabuleiro()

            print(f"Vez do {self.turno}, Qual sua Jogada?")

            while True:
                jogada = input("Jogada: ")

                if self.verificarjogada(jogada): # se a jogada for Válida...
                    break # Encerra o loop
                else:
                    print(f"Jogada do {self.turno} Invalida, jogue Novamente.")
            self.tabuleiro[jogada] = self.turno

            estado = self.verificartabuleiro()

            if estado == "X":
                os.system('cls')
                print("X Venceu")
                self.exibirtabuleiro()
                self.jogar_novamente()
                break

            elif estado == "O":
                os.system('cls')
                print("O Venceu")
                self.exibirtabuleiro()
                self.jogar_novamente()
                break
                
            elif estado == "empate":
                os.system('cls')
                print("Empate!!!")
                self.exibirtabuleiro()
                self.jogar_novamente()
                break
            
               

            # Trocar Jogador
            self.turno = "X" if self.turno == "O" else "O"
        
        self.exibirtabuleiro()

    def reiniciar_jogo(self):
        __init__()
    
    def jogar_novamente(self):
        while True:
            print(f"Gostaria de jogar novamente? S / N ")

            jogada = input()
            if jogada.upper() in ('S','N'):
                if jogada.upper() == 'S':
                    os.system('cls')
                    self.reiniciar_jogo()
                else:
                    exit()
            else:
                print(f"Opção invalida")

#%%
class JogoDaVelha1xpc(JogoDaVelha1x1):
    tabuleiro = {'7':' ','8':' ','9':' ',
                 '4':' ','5':' ','6':' ',
                 '1':' ','2':' ','3':' '}
    turno = None

    def __init__(self, jogador_inicial="player"):
        self.turno = jogador_inicial
        self.tabuleiro = {'7':' ','8':' ','9':' ',
                 '4':' ','5':' ','6':' ',
                 '1':' ','2':' ','3':' '}
        
  
    def jogadaDisponivel(self):
        jodagadisponivel = []
        for i in self.tabuleiro.keys():
            if self.tabuleiro[i] == " ":
                jodagadisponivel += str(i)
        return jodagadisponivel
    
    def jogadopc(self):
        jogada_disponivel = self.jogadaDisponivel()
        jogada_pc = random.choice(jogada_disponivel)
        return jogada_pc

    def verificaestado(self,estado):
        if estado == "X":
            os.system('cls')
            print("X Venceu")
            self.exibirtabuleiro()
            self.jogar_novamente()
            return False

        elif estado == "O":
            os.system('cls')
            print("O Venceu")
            self.exibirtabuleiro()
            self.jogar_novamente()
            return False
                    
        elif estado == "empate":
            os.system('cls')
            print("Empate!!!")
            self.exibirtabuleiro()
            self.jogar_novamente()
            return False
                
    def jogar(self,jogadorpc,jogador):
        while True:
            
            os.system('cls') 
            self.exibirtabuleiro()

            print(f"{self.turno} vez")

            if self.turno == 'PC' and jogadorpc == 'X':
                
                time.sleep(2)
                print(f"PC jogou X :")

                jogadapc = self.jogadopc()

                self.tabuleiro[jogadapc] = jogadorpc

                estado = self.verificartabuleiro()
                self.verificaestado(estado)
            
            elif self.turno == 'player' and jogador == 'X':
                
                print(f"Qual sua Jogada?")

                while True:
                    jogada = input("Jogada: ")

                    if self.verificarjogada(jogada): # se a jogada for Válida...
                        break # Encerra o loop
                    else:
                        print(f"Jogada do {self.turno} Invalida, jogue Novamente.")

                self.tabuleiro[jogada] = jogador
                estado = self.verificartabuleiro()
                self.verificaestado(estado)
                

            elif self.turno == 'PC' and jogadorpc == 'O':

                time.sleep(2)
                print(f"PC jogou O :")

                jogadapc = self.jogadopc()

                self.tabuleiro[jogadapc] = jogadorpc
                
                estado = self.verificartabuleiro()
                self.verificaestado(estado)
            
            elif self.turno == 'player' and jogador == 'O':
                print(f"Qual sua Jogada?")

                while True:
                    jogada = input("Jogada: ")

                    if self.verificarjogada(jogada): # se a jogada for Válida...
                        break # Encerra o loop
                    else:
                        print(f"Jogada do {self.turno} Invalida, jogue Novamente.")
                    
                self.tabuleiro[jogada] = jogador
                estado = self.verificartabuleiro()
                self.verificaestado(estado)

            # Trocar Jogador
            self.turno = "PC" if self.turno == "player" else "player"
            
        self.exibirtabuleiro()
#%%

def jogo1x1():
    jogo = JogoDaVelha1x1()
    jogo.jogar()

def jogo1xpc(jogadorpc,jogador):
    jogo = JogoDaVelha1xpc()
    jogo.jogar(jogadorpc,jogador)


def __init__():
    while True:
        os.system('cls')
        print("╬ Instrucões do Jogo ╬")
        print("Utilize a posição do teclado numérico para realizar suas jogadas")
        print("┌───┬───┬───┐")
        print("| 7 | 8 | 9 |")
        print("├───┼───┼───┤")
        print("| 4 | 5 | 6 |")
        print("├───┼───┼───┤")
        print("| 1 | 2 | 3 |")
        print("└───┴───┴───┘")
        print("")
        print("")
        print('Escolha a modalidade do Game:')
        print('')
        print('1 - Jogo 1x1')
        print('2 - Jogo 1xPC')

        jogotipo = int(input())

        if jogotipo in (1,2):
            if jogotipo == 1:
                jogo1x1()
            else:
                while True:
                    print(f"Você deseja jogar como:")
                    print("X ou O")

                    jogador = input()

                    if jogador.upper() in ("X","O"):
                        if jogador.upper() == "X":
                            jogadorpc = "O"
                        else:
                            jogadorpc = "X"
                        os.system('cls')
                        jogo1xpc(jogadorpc,jogador)
                    else:
                        print(f"Opção Invalida, Selecione o jogador entre X ou O")
        else:
            print(f"Opção Invalida, Selecione 1 ou 2")
        
    
__init__()
    

    

# %%

# %%
