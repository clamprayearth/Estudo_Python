from os import system , name
"""Todas as funções tem como parametro as variáveis n# que são a quantidade de notas. Funciona como
variaveis globais num contexto de funções puras. OBS: Menos limpatela()"""

def zerarCofrinho(n100, n50, n20, n10, n5, n2, n1):
    """Função que retira todo o conteudo do cofrinho"""
    n100 = 0 
    n50 = 0 
    n20 = 0 
    n10 = 0 
    n5 = 0 
    n2 = 0 
    n1 = 0

def limpaTela ():
    """Função limpa tela para o usuário"""
    if name == 'nt':
        system('cls')
    else:
        system('clear ')
#Todas as variáveis que tenham x como nome será apenas para parada de tela.

def cedulas(n100, n50, n20, n10, n5, n2, n1):
    """Função para dá valores em R$ as cedulas no cofrinho"""
    return (n100*100), (n50*50), (n20*20), (n10*10), (n5*5), (n2*2), n1

def total(n100, n50, n20, n10, n5, n2, n1):
    """Função que diz o valor total das cedulas"""
    nota100, nota50, nota20, nota10, nota5, nota2, nota1 = cedulas(n100, n50, n20, n10, n5, n2, n1)
    return nota100+nota50+nota20+nota10+nota5+nota2+nota1
#Todas as variáveis que tenham y como nome é para receber o valor total do saldo.

def retirar(respo, n100, n50, n20, n10, n5, n2, n1, nota100 = 0, nota50 = 0, nota20 = 0, nota10 = 0, nota5 = 0, nota2 = 0, nota1 = 0):
    """"Função que verifica as notas e retira elas do saldo total"""
    if (type(respo) == int):               
        if (respo >= 100) and (n100 != 0) and (nota100 < n100):
            nota100 += 1                   #Esse if calcula quantas notas são necessario para efetuar o saque,
            aux = respo - 100              #sempre diminuido o valor do saque até zero.
            respo = aux
        elif (respo >= 50) and (n50 != 0) and (nota50 < n50):
            nota50 += 1
            aux = respo - 50
            respo = aux
        elif (respo >= 20) and (n20 != 0) and (nota20 < n20): 
            nota20 += 1
            aux = respo - 20
            respo = aux
        elif (respo >= 10) and (n10 != 0) and (nota10 < n10):
            nota10 += 1
            aux = respo - 10
            respo = aux
        elif (respo >= 5) and (n5 != 0) and (nota5 < n5):
            nota5 += 1
            aux = respo - 5
            respo = aux
        elif (respo >= 2) and (n2 != 0) and (nota2 < n2):
            nota2 += 1
            aux = respo - 2
            respo = aux 
        elif (respo >= 1) and (n1 != 0) and (nota1 < n1):
            nota1 += 1
            aux = respo - 1
            respo = aux
        
        if (respo == 0): #Caso o saque chegue a zero o programa sai da recusividade
            if (n100 >= nota100) and (n50 >= nota50) and (n20 >= nota20) and (n10 >= nota10) and (n5 >= nota5) and (n2 >= nota2):
                n100 -= nota100             #Esse if faz a diferença entre as notas necessárias e as disponiveis.
                n50 -= nota50               #Caso não bater as notas o programa apresenta um erro.
                n20 -= nota20
                n10 -= nota10
                n5 -= nota5
                n2 -= nota2
                n1 -= nota1
                
                y = total(n100, n50, n20, n10, n5, n2, n1)
                
                limpaTela() #Função para limpar tela
                print("--------------------------------------")
                print("Operação realizada com sucesso.")
                if (nota100 > 0):                   #Aqui é impresso as notas uma a uma.
                    print("R$100\n"*nota100)
                if (nota50 > 0):
                    print("R$50\n"*nota50)
                if (nota20 > 0):
                    print("R$20\n"*nota20)
                if (nota10 > 0):
                    print("R$10\n"*nota10)
                if (nota5 > 0):
                    print("R$5\n"*nota5)
                if (nota2 > 0):
                    print("R$2\n"*nota2)
                if (nota1 > 0):
                    print("R$1\n"*nota1)
                print("Novo Saldo: R${}".format(y))
                print("--------------------------------------")
                x = input("--> Enter para continuar ...") #Essa variável é para a parada de tele apenas
                main(n100, n50, n20, n10, n5, n2, n1)
            else:
                limpaTela() #Função para limpar tela
                print("--------------------------------------")
                print("Não há notas para o saque ou saldo=0!")
                print("Operação não realizada.")
                print("--------------------------------------")
                x = input("--> Enter para continuar ...") #Essa variável é para a parada de tele apenas
                main(n100, n50, n20, n10, n5, n2, n1)
        else:
            retirar(respo, n100, n50, n20, n10, n5, n2, n1, nota100, nota50, nota20, nota10, nota5, nota2, nota1)

def depositar(n100, n50, n20, n10, n5, n2, n1):
    """Função para depositar valores no cofrinho"""
    limpaTela() #Função para limpar tela
    print("--------------------------------------")
    print("Qual nota deseja depositar?")
    print("R$100 -> A; R$50 -> B; R$20 -> C; R$10 -> D; R$5 -> E; R$2 -> F; R$1 -> G")
    print("--------------------------------------")
    nota = input()
    qts = int(input("Quantas notas ao todo?"))
    
    if (nota == "A") or (nota == "a"):
        n100 += qts
    elif (nota == "B") or (nota == "b"):
        n50 += qts
    elif (nota == "C") or (nota == "c"):
        n20 += qts
    elif (nota == "D") or (nota == "d"):
        n10 += qts
    elif (nota == "E") or (nota == "e"):
        n5 += qts
    elif (nota == "F") or (nota == "f"):
        n2 += qts
    elif (nota == "G") or (nota == "g"):
        n1 += qts
    else:
        print("Nota não computada!")
        x = input("--> Enter para continuar ...") #Essa variável é para a parada de tele apenas
        depositar(n100, n50, n20, n10, n5, n2, n1)
    limpaTela() #Função para limpar tela
    
    y = total(n100, n50, n20, n10, n5, n2, n1)

    print("Deposito realizado com sucesso!")
    print("Novo Saldo: {}".format(y))
    respo = input("Deseja realizar novo deposito? S/N: ")
    print("--------------------------------------")
    if (respo == "S") or (respo =="s"):
        depositar(n100, n50, n20, n10, n5, n2, n1)
    else:
         main(n100, n50, n20, n10, n5, n2, n1)   

def sacar(n100, n50, n20, n10, n5, n2, n1):
    """Função para sacar no cofrinho"""
    limpaTela() #Função para limpar tela
    print("--------------------------------------")
    print("Quanto deseja sacar?")
    print("Coloque somente valores inteiros. Não deve-se usar moedas!")
    print("--------------------------------------")
    respo = int(input())

    y = total(n100, n50, n20, n10, n5, n2, n1)

    if (y == 0):
        limpaTela() #Função para limpar tela
        print("--------------------------------------")
        print("Não existe saldo!")
        print("--------------------------------------")
        x = input("--> Enter para continuar ...") #Essa variável é para a parada de tele apenas
        main(n100, n50, n20, n10, n5, n2, n1)
    elif (respo > y):
        limpaTela() #Função para limpar tela
        print("Saldo insuficiente!")
        print("Saldo Atual: R${}".format(y))
        respo2 = input("Deseja retirar todo o valor S/N: ")
        if (respo2 == "S") or (respo2 == "s"):
            zerarCofrinho(n100, n50, n20, n10, n5, n2, n1)
        main(n100, n50, n20, n10, n5, n2, n1)
    else:
        retirar(respo,n100, n50, n20, n10, n5, n2, n1)
    
def saldo(n100, n50, n20, n10, n5, n2, n1):
    """Função que retorna o saldo total do cliente"""
    limpaTela() #Função para limpar tela
    y = total(n100, n50, n20, n10, n5, n2, n1)
    print("--------------------------------------")
    print("Saldo Atual: R${}".format(y))
    print("--------------------------------------")
    x = input("--> Enter para continuar ...") #Essa variável é para a parada de tele apenas
    main(n100, n50, n20, n10, n5, n2, n1) 

def relatorio(n100, n50, n20, n10, n5, n2, n1):
    """Função que exibe o relatorio das notas"""
    limpaTela() #Função para limpar tela
    print("+---------------------------+")
    print("| Relatório geral |")
    print("+---------------------------+")
    print("Notas de R$100,00: {}".format(n100))
    print("Notas de R$50,00:  {}".format(n50))
    print("Notas de R$20,00:  {}".format(n20))
    print("Notas de R$10,00:  {}".format(n10))
    print("Notas de R$5,00:   {}".format(n5))
    print("Notas de R$2,00:   {}".format(n2))
    print("Notas de R$1,00:   {}".format(n1))
    x = input("--> Enter para continuar ...") #Essa variável é para a parada de tele apenas
    main(n100, n50, n20, n10, n5, n2, n1)

def main(n100, n50, n20, n10, n5, n2, n1):
    """Função de tela principal"""
    limpaTela() #Função para limpar tela
    print("--------------------------------------")  
    print("1 - Depositar")
    print("2 - Sacar")
    print("3 - Saldo")
    print("4 - Relatório")
    print("5 - Finalizar")
    print("--------------------------------------")
    esco = input("Escolha uma opcao:")

    y = total(n100, n50, n20, n10, n5, n2, n1)

    if (esco == "1"):
        depositar(n100, n50, n20, n10, n5, n2, n1)
    elif (esco == "2"):
        sacar(n100, n50, n20, n10, n5, n2, n1)
    elif (esco == "3"):
        saldo(n100, n50, n20, n10, n5, n2, n1)
    elif (esco == "4"):
        relatorio(n100, n50, n20, n10, n5, n2, n1)
    elif (esco == "5"):
        print("Saldo Atual: R${}".format(y))
        if (y > 0):
            respo2 = input("Deseja retirar todo o valor S/N: ")
            if (respo2 == "S") or (respo2 == "s"):
                retirar(y, n100, n50, n20, n10, n5, n2, n1)
            else:
                exit()
    else:
        main(n100, n50, n20, n10, n5, n2, n1)
main(1,1,1,1,1,1,1) 
