O jogo de xadrez possui várias peças com movimentos curiosos: uma delas é a dama, que pode se mover qualquer quantidade de casas na mesma linha, na mesma coluna, ou em uma das duas diagonais

O grande mestre de xadrez Kary Gasparov inventou um novo tipo de problema de xadrez: dada a posição de uma dama em um tabuleiro de xadrez vazio (ou seja, um tabuleiro 8 × 8, com 64 casas), de quantos movimentos, no mínimo, ela precisa para chegar em outra casa do tabuleiro?

Kary achou a solução para alguns desses problemas, mas teve dificuldade com outros, e por isso pediu que você escrevesse um programa que resolve esse tipo de problema

Saída
Para cada caso de teste da entrada seu programa deve imprimir uma única linha na saída, contendo um número inteiro, indicando o menor número de movimentos necessários para a dama chegar em sua casa de destino.

# O Número max de movimentos para a dama percorrer o tabuleiro é de dois movimento
# 0 -> se quiser ficar na msm posição 
# 1 -> se ela estiver na diagonal, horizontal ou vertical
# 2 -> caso contrário

Exemplo de Entrada
4 4 6 2
3 5 3 5
5 5 4 3
0 0 0 0

Exemplo de Saída
1
0
2