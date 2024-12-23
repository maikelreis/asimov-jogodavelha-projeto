# 🎮 Projeto Jogo da Velha em Python

## 📖 Sobre o Projeto
Este é um clássico jogo da velha (ou "tic-tac-toe") implementado em Python. Com suporte para partidas entre dois jogadores ou contra a CPU, o projeto foi desenvolvido como parte do curso Python Starter - ASIMOV para praticar conceitos de lógica, classes e interação com o usuário.

## 🎯 Funcionalidades
-  Modos de Jogo:
    - 1x1: Dois jogadores se enfrentam.
    - 1xPC: Enfrente a CPU com escolhas automáticas.

-  Tabuleiro Visual:
    - O tabuleiro é exibido de maneira intuitiva no console, utilizando o formato de teclado numérico para as jogadas.

-  Controle de Turnos:
    - Alternância automática entre os jogadores ou entre você e o PC.

-  Detecção de Vencedor ou Empate:

    - Verifica condições de vitória (linhas, colunas ou diagonais).
    - Reconhece situações de empate.

  - Reiniciar Jogo:
    - Após uma partida, você pode decidir se quer jogar novamente ou encerrar.

## 🛠️ Tecnologias Utilizadas

- Linguagem: Python.
- Bibliotecas:
  - ``random`` para jogadas automáticas do PC.
  - ``time`` para atrasos controlados nas jogadas da CPU.
  - ``os`` para limpar a tela no console, melhorando a experiência visual.

## 📂 Estrutura do Projeto
 - JogoDaVelha1x1: Classe para partidas entre dois jogadores.
 - JogoDaVelha1xPC: Subclasse para partidas contra o computador.
 - Funções principais:
     - ``jogo1x1()``: Inicia o modo 1x1.
     - ``jogo1xpc(jogadorpc, jogador)``: Inicia o modo contra o PC.
     - ``__init__()``: Gerencia o menu inicial e a escolha do modo de jogo.

## 📜 Instruções
  1. Instale o Python: Certifique-se de ter o Python 3.x instalado em sua máquina.
  2. Execute o Jogo:
    Salve o código em um arquivo chamado jogo_da_velha.py e rode o script:
    
    python tic-tae-toe.py
    
  3. Como Jogar:
     - Escolha o modo de jogo no menu inicial (1x1 ou 1xPC).
     - Use o teclado numérico para fazer suas jogadas:
     - Para cada turno, escolha a posição onde deseja jogar.

## 🔮 Melhorias Futuras
- Adicionar dificuldade configurável para o PC (fácil, médio, difícil).
- Implementar uma interface gráfica usando bibliotecas como Tkinter ou Pygame.
- Salvar o histórico de jogos para análise posterior.

