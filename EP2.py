from os import system , name
import matplotlib.pyplot as plt
import numpy as np
import math

def equacao(x):
    """Fucao que determina qual sera a equacao utilizada"""
    Fxa = math.sin(x) + math.cos(x) #<- Coloque a equacao escolhida aqui        
    return Fxa, "Sen(x) + Cos(x)"                                            #<-Foi necessario a construção de duas funções
def equacao2(x):                                                             #uma retornando só o resultado e outra uma string
    """Fucao que determina qual sera a equacao utilizada"""                  #Tudo isso para os gráficos abaixo.
    Fxa = math.sin(x) + math.cos(x) #<- Coloque a equacao escolhida aqui
    return Fxa    

def derivada(x):
    """Fucao que determina qual sera a derivada utilizada"""
    Dxa = math.cos(x) - math.sin(x)     #<- Coloque a derivada da funcao anterior aqui
    return Dxa, "Cos(x) - Sen(x)"

def tolerancia(fy):
    """Fucao que determina qual sera a tolerancia"""
    if (fy<=1/(10**15)):
        return True
    else:
        return False

def Bissecao(a=3, b=0, i=1, l = [], la = [], ly =[]):
    """Funcao que aplica o metodo da bissesao"""
    x=(a + b) / 2         #<- Os valores de a, b, f(x) e desvio de erro
    y=(a - b) / 2          #sao amarzenados nestas listas
    la += [i]
    eN, eS = equacao(x)                     
    if (eN==0) or (i==100) or (tolerancia(y)): #<- Esse if que aplica a logica
        return l + [x], la, ly + [y]        #do metodo da Bissesao.
    else:
        if (eN > 0):            
            return Bissecao(a, x, i+1, l + [x], la, ly+ [y])
        elif (eN < 0):
            return Bissecao(x, b, i+1, l + [x], la, ly + [y])

def newton_raphson(i=1, a=3, l=[], la=[], ly=[]):
    """Funcao que aplica o metodo Newton-Raphson"""
    eN, eS = equacao(a)
    dN, dS = derivada(a)
    fx = a-(eN/dN) #<- Aplicacao da formula de Newton-Raphson
    fy = (fx-a)/fx  #<- Aplicacao do desvio de erro
    if (fy<0):  #<- if que faz o resultado ser em modulo 
        fy = fy*-1
    if (i==100) or (tolerancia(fy)) or (eN==0):
        return l, la, ly
    else:
        return newton_raphson(i+1, fx, l+[fx], la + [i], ly+[fy])

def secante(i=1, a=0, b=3, l=[], la=[], ly=[]):
    """Funcao que aplica o metodo da Secante"""
    eN, eS = equacao(a)
    dN, dS = derivada(a)
    eN1, eS1 = equacao(b)
    fx = ((b*eN)-(a*eN1))/(eN-eN1)  #<- Aplicacao da formula da secante
    fy = (fx-b)/fx   #<- Aplicacao do desvio de erro
    if (fy<0):  #<- if que faz o resultado ser em modulo
        fy = fy*-1
    if (i==100) or (tolerancia(fy)) or (eN==0): 
        return l, la, ly
    else:
        return secante(i+1, b, fx, l+[fx], la+[i], ly+[fy])

def relatorio(y, x, ly, i=0):
    """Fusao que imprime as raizes geradas e seus erros"""
    if (i<=len(x)-1):
        print("---------------------------------------------------")
        print("{}  Raiz:{:.15f}  Erro:{:.15f}".format(x[i], y[i], ly[i]))
        relatorio(y, x, ly, i+1)


def main():
    """Fusao principal do programa""" 
    y1, x1, ly1 = Bissecao()       #<- Chamada dos metodos
    y2, x2, ly2 = newton_raphson() #aqui é onde se armazena todos os resultados do programa
    y3, x3, ly3 = secante()
    eN, eS = equacao(2)
    dN, dS = derivada(2)
    
    if name == 'nt':    #<-Nesse if a tela é limpa
        system('cls')
    else:
        system('clear ')

    print("Função escolhida: f(x) = {}".format(eS))  #<-Relatorio##################################################
    print("Derivada: f'(x) =  {}".format(dS))
    print("Número máximo de iterações: 100")
    print("Tolerância: 1/10**15")
    print("")

    print("Metodo da Bissecao: a = 1 e b = 3")
    relatorio(y1, x1, ly1)
    print("---------------------------------------------------")
    print("")
    print("Metodo de Newton-Raphson: x1 = 3")
    relatorio(y2, x2, ly2)
    print("---------------------------------------------------")
    print("")
    print("Metodo da Secante: x1 = 1 e x2 = 3")
    relatorio(y3, x3, ly3)
    print("---------------------------------------------------")
    print("")
    print("")                                  #<-Relatorio##################################################

    r = input("Deseja imprimir os graficos da função? S/N ")
    if (r == "S") or (r == "s"): 
###################################### Grafico Geral ######################################
        x=np.arange(-8, 8)
        y=np.arange(-8,8)
        yN = list(map(equacao2, y))

        fig, ax = plt.subplots()
        ax.plot(x, yN)

        ax.set(xlabel='x', ylabel='y',
        title='$f(x) = {}$'.format(eS))
        ax.grid(20)

        fig.savefig('ep2_graficoGeral.pdf',bbox_inches='tight') #salva o gráfico
        plt.show()

    ###################################### Grafico aproximacao raiz ######################################
        fig = plt.figure(figsize=(10,5))
        ax = fig.add_subplot(111)
        ax.plot(x1[:15], y1[:15], label='Bisseção', lw=1, markersize=6, color='#9467BD', marker='D', markeredgecolor='#9467BD', markerfacecolor='#C9B3DE')
        ax.plot(x2, y2, label='Newton', lw=1, markersize=6, color='#1F77B4', marker='o', markeredgecolor='#1F77B4', markerfacecolor='#8FBBD9')
        ax.plot(x3, y3, label='Secante', lw=1, markersize=6, color='#D62728', marker='s', markeredgecolor='#D62728', markerfacecolor='#EA9393')
    
        #Legenda
        handles, labels = ax.get_legend_handles_labels()
        leg = ax.legend(handles, labels, bbox_to_anchor=(1.01, 1), loc=2, borderaxespad=0.)
    
        ax.set(xlabel='Iteração', ylabel='$f(x)$', title=r"Aproximação da raiz de $f(x) = {}$".format(eS))
        ax.grid()
    
        #Exibe todos os valores das iteração.
        plt.xticks(x1[:15])  #Troque x1 pelo método que tiver maior número de iterações. Talvez comentar essa linha fique melhor para o seu gráfico.
    
        plt.savefig('ep2_graficoRaiz.pdf',bbox_inches='tight') #salva o gráfico
        plt.show()
   
  
        ###################################### Grafico erro relativo ######################################
        y1=float(("{:.15f}".format(ly1[len(ly1)-1]))) #<- Aqui foi nescessario truncar os resultados para
        y2=float(("{:.15f}".format(ly2[len(ly2)-1]))) #que os valores entre os erros sejam visiveis no grafico
        y3=float(("{:.15f}".format(ly3[len(ly3)-1])))
        x = [1, 2, 3]
        y = [y1, y2, y3]
    
        fig, ax = plt.subplots(figsize=(10, 5))

        ax.bar(x, y, color='#1F77B4')

        # ax.set_xlabel('Método', fontsize = 12)
        ax.set_ylabel('y', fontsize = 12)
        ax.set_title('Erro Relativo', fontsize = 12)
        ax.set_axisbelow(True) 
        ax.yaxis.grid(True)

        ax.set_xticks(x)
        ax.set_xticklabels(('Bisseção', 'Newton', 'Secante'))

        plt.ylim(0, 0.0000000001) #<- valor limite do eixo y obs:Teve que ser muito pequeno para que 
                                 # as diferencas ente os erros relativos sejam visiveis.
        plt.savefig('ep2_graficoErros.pdf',bbox_inches='tight') #salva o gráfico
        plt.show()
    #####################################################################################
# Executa a função principal do projeto
main()