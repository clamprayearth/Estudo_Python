"""
Problema: Crie uma função em python que retorne a parte Par e a parte Impar de um sinal qualquer e teste nos sinais:
                a. s1 = [ 2, 1, 0, 1, 2], n = [-2, -1, 0, 1, 2]
                b. s2 = [-2,-1, 0, 1, 2], n = [-2, -1, 0, 1, 2]
                c. s3 = [ 0, 0 ,0 , 2, 4], n = [-2, -1, 0, 1, 2]
                d. s4 = [ 0 , -1 , -1, 3 , 2], n = [-2, -1, 0, 1, 2]
                e. s5 = [ 0, 0 ,0 , 2, 4], n = [ 0, 1, 2, 3, 4]
Modelo da função:
    p,i = separa ParImpar(x,n)
     Entrada:
        x – sinal de entrada  
        n – vetor de tempo do sinal de entrada
     Saída:
        p – parte par do sinal
        i – parte impar do sinal

Versão: 0.1
Data: 05/03/2021
Autor: Antonio Alves dos Santos Neto
Arquivo: sinais_par_impar.py
Objetivo: Lista de exercicio questão 1 de Processamento digital de sinais para avaliação
"""
#Declaração de bibliotecas
import numpy as np
from numpy import pi
import matplotlib.pyplot as plt

def separarParImpar(sinal, tempo): 
    #Variavel que calcula o tamanho do vetor sinal
    tam = len(sinal)

    #Aqui eu converto o vetor sinal para float e tempo para inteiro
    for i in range(tam):
        sinal[i] = float(sinal[i])
        tempo[i] = int(tempo[i])
    
    #Só é permitida a execuçáo do código caso o vetor sinal e tempo tiverem o mesmo tamanho
    if(len(sinal) == len(tempo)):
        #Sinais par e impar
        sinal_par = []
        sinal_impar = []

        #Aqui aplica-se a formula de um sinal par e um sinal impar
        for i in range(tam):
            aux = (1/2) * sinal[i]
            aux2 = (1/2) * sinal[tam-1-i]  
            sinal_par.append(aux+aux2)
            sinal_impar.append(aux-aux2)

        return sinal_par, sinal_impar
    else:
        print("Dados inconsistentes")

def grafico(sinal, tempo, par, impar):
    yD1 = par
    yD2 = impar
    n = tempo
    print("Sinal: {}\nTempo: {}".format(sinal, n))
    #criando os gráficos
    fig, ax = plt.subplots(3,1)
    ax[0].stem(n, sinal, linefmt='b-',use_line_collection=True)
    ax[0].set_xlabel("Amostras")
    ax[0].set_ylabel("Amplitude")
    ax[0].grid(True)
    ax[0].set_title('Sinal')
    ax[1].stem(n, yD1, linefmt='b-',use_line_collection=True)
    ax[1].set_xlabel("Amostras")
    ax[1].set_ylabel("Amplitude")
    ax[1].grid(True)
    ax[1].set_title('Sinal Par')
    ax[2].stem(n, yD2, linefmt='b-',use_line_collection=True)
    ax[2].set_xlabel("Amostras")
    ax[2].set_ylabel("Amplitude")
    ax[2].grid(True)
    ax[2].set_title('Sinal Impar')
    fig.tight_layout()
    plt.show()

"""A variavel linha é reutilizada para o vetor sinal e tempo (ela é usada apenas para pegar o valor da linha que o usario escreve)
linha = input("Enre com o sinal (os valores são separados por espaço): "); #--> Entrada de dados (valores para o vetor sinal)
x = linha.split()
linha = input("Enre com o tempo (os valores são separados por espaço): "); #--> Entrada de dados (valores para o vetor tempo)
n = linha.split()
"""

#Caso se queira que colocar os valores em tempo de execução descomente a linha acima e comete essas no paragrafo
x = [0, 0 ,0 , 2, 4] #--> Coloque os valores do sinal aqui
n = [0, 1, 2, 3, 4] #--> Coloque os valores da amostra aqui

p, i = separarParImpar(x, n)
grafico(x, n, p, i)



