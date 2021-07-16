"""
Problema: Imagine uma lista de compras. Ela possui:
            Itens
            Quantidade de cada item
            Preço por unidade/peso/pacote de cada item
          Desenvolva uma função (ou método) que irá receber uma lista de compras (como a detalhada 
          acima) e uma lista de e-mails. Aqui, cada e-mail representa uma pessoa. A função deve:
            Calcular a soma dos valores, ou seja, multiplicar o preço de cada item por sua quantidade e somar todos os itens
            Dividir o valor de forma igual entre a quantidade de e-mails
            Retornar um mapa/dicionário onde a chave será o e-mail e o valor será quanto ele deve pagar nessa conta
Versão: 0.1
Data: 18/01/2021
Autor: Antonio Alves dos Santos Neto
obs: Antes de mais nada eu trabalhei com o paradigma de programação
funcional onde eu passo listas como argumento de funções para 
não usar variaveis globais
obs2: Para que o usario não sai do programa é chamada a função main sempre no final de 
cada bloco de notas e limpa-se a tela.
"""
from os import system , name

def limpaTela():
    """Função limpa tela para deixar uma certa estética ao programa.
    Dependendo do sistema operacional ele escolhe o comando a ser dado"""
    if name == 'nt':
        system('cls')
    else:
        system('clear ')

def paradaTela():
    #Função para parada de tela
     x = input("\n--> Enter para continuar ...") #Essa variável é para a parada de tele apenas

def visualPedido(email, itens):
    #Função que imprimi o pedido na tela
    limpaTela() #Função para limpar tela
    print("+---------------------------+")
    print("| Relatório pedido |")
    print("+---------------------------+")
    print("Emails: ")
    for e in email:
        print("{} ".format(e))
    """Os espaços é para que as colunas fiquem alinhadas
    Transformo os preços para decimal para que o usuario visualize"""
    print("\nItem    qtd    Uni    Pes    Pct")
    """A variavel x é para gerar uma lista chamada interacao onde ela é usada para 
    percorrer a lista itens pelo indice"""
    x = -1
    interacao = []
    for i in (itens):
        x += 1
        interacao.append(int(x)) 
    #Coloquei essa parte do codigo para que não multiplique o nome e quantidade por 100
    for i in (interacao):
        aux = 0
        while(aux < 5):
            if(aux>1):
                print("{:.2f}    ".format(float(itens[i][aux]/100)), end='')
            else:
                print("{}    ".format(itens[i][aux]), end='')
            aux += 1
        print("")
    paradaTela()
    main(email, itens)

def inserir(email, itens):
    #Função para a inserção de itens no pedido
    limpaTela() #Função para limpar tela

    #Para que o haja o inclusão é necessario que tenha pelo menos um email cadastrado
    if len(email) != 0:
        #Aqui é onde armazeno as entradas do usuarios e depois coloco em uma lista
        nome = input("Nome: ")
        quant = int(input("Quantidade: "))
        print("Coloque os inteiros e decimais separados por ponto e os valores em reais e centavos")
        print("Ex: 4.60 = Quatro reais e sesenta centavos; 12.00 = doze reais")
        preco_uni = float(input("Preço Unidade: "))
        preco_peso = float(input("Preço Peso: "))
        preco_paco = float(input("Preço Pacote: "))

        #Transformação de decimal para inteiro
        preco_uni = int(preco_uni*100)
        preco_peso = int(preco_peso*100)
        preco_paco = int(preco_paco*100)
    
        itens += ([nome, quant, preco_uni, preco_peso, preco_paco],)
        print("Inserção de item com sucesso")
        paradaTela()
    else:
        print("Necessario cadastrar email de cliente")
        paradaTela()

    main(email, itens) 

def exclusao(lista):
    #Para que o haja o exclusão é necessario que tenha pelo menos um registro cadastrado
    if len(lista) != 0:
        """Usei essa variavel j para mostrar o valor dos indices da lista 
        paro o usuario, ela se incrementa a cada time para indicar os indices"""
        j = -1
        print("Registros: ")
        for i in (lista):
            j+=1
            print(" {} - {}".format(j,i))
        """Foi necessario fazer uma conversão explicita para inteiro 
        aqui para não conflitar com o indice da lista"""
        esco = int(input("Escolha uma opcao entre os numerais na frente do registro ou -1 para sair:"))
        if (esco > -1) and (esco < len(lista)):
            lista.remove(lista[esco])
            print("Exclusão de registro com sucesso")
            paradaTela()
        else:
            print("Exclusão não efetuada")
            paradaTela()
    else:
        paradaTela()
    
    return lista

def delete(email, itens):
    #Função para excluir itens do pedido
    limpaTela() #Função para limpar tela

    itens = exclusao(itens)
    
    main(email, itens)

def mailInserir(email, itens):
       #Função para a inserção de emails de clientes
    limpaTela() #Função para limpar tela

    print("Cadastro de clientes")
    climail = input("E-mail: ") 
    email += (climail,)
    limpaTela() #Função para limpar tela
    print("Inserção de email com sucesso")
    paradaTela()
    main(email, itens)

def mailDeletar(email, itens):
     #Função para a exclusão de emails de clientes
    limpaTela() #Função para limpar tela

    email = exclusao(email)
    main(email, itens)

def finalizar(email, itens):
    #Função que fecha e calcula o preço a pagar de cada cliente
    limpaTela() #Função para limpar tela
    
    #Inicialização do preço total a pagar
    preco = 0
    """A variavel x é para gerar uma lista chamada interacao onde ela é usada para 
    percorrer a lista itens pelo indice"""
    x = -1
    interacao = []
    #Dicionario onde vai ficar o preço a pagar de cada usuario
    clientes = {}
    for i in (itens):
        x += 1
        interacao.append(int(x)) 

    if (len(email) != 0) and (len(itens) != 0):
        print("2 -> Unidade") 
        print("3 -> Peso") 
        print("4 -> Pacote")
        esco = int(input("Deseja utilizar quais preços para calcular o valor do pedido?: "))
        for i in interacao:
            preco += int(itens[i][1] * itens[i][esco]) 

        """Para calcular o valor a pagar eu pego um valor redondo com
        o numero de clientes. Depois eu retiro o resto que falta e incremento de um
        em um para cada cliente""" 
        if (preco%len(email) == 0):
            preco = preco / len(email)
            #Tranformo o valor de inteiro para decimal(reais,centavos)
            preco = preco / 100
            #Crio o dicionario como chave o email do cliente
            for i in email:
                clientes[i] = preco 
            return clientes
        else:
            resto = preco%len(email)
            preco = preco - resto
            preco = int(preco / len(email))
            
            #Foi necessario criar essas variaveis adicionais para o incremento do resto
            aux_list = []
            interacao.clear()
            x = -1

            """Utilizei novamente a lista interação para usar na 
            interação de preco a pagar de cada cliente. Utilizando uma lista auxiliar"""
            for i in (email):
                x += 1
                interacao.append(int(x))
            
            #Aqui eu dou para todos os clientes o preço redondo
            for i in (interacao):
                    aux_list.append(int(preco))
            #Depois a o incremento do resto para cada ocorrencia
            x = 0
            while (resto !=0):
                aux_list[x] = preco + 1
                x += 1
                resto -= 1
            #Tranformo o valor de inteiro para decimal(reais,centavos)
            for i in (interacao):
                aux_list[i] = aux_list[i] / 100
            #Crio o dicionario como chave o email do cliente
            x = 0
            for i in (email):
                clientes[i] = aux_list[x]
                x += 1

            return clientes
    elif(len(email) == 0) or (len(itens) == 0):
        print("Pedido incompleto")
        paradaTela()
        main(email, itens) 

def main(email, itens):
     #Função de tela principal
    limpaTela() #Função para limpar tela
    print("--------------------------------------")  
    print("1 - Inserir Item")
    print("2 - Remover Item")
    print("3 - Inserir Email")
    print("4 - Remover Email")
    print("5 - Visualisar Pedido")
    print("6 - Fechar pedido")
    print("7 - Sair")
    print("--------------------------------------")
    esco = input("Escolha uma opcao:")

    #Aqui é onde o programa decide o que fazer com as respostas dadas
    if (esco == "1"):
        inserir(email, itens)
    elif (esco == "2"):
        delete(email, itens)
    elif (esco == "3"):
        mailInserir(email, itens)
    elif (esco == "4"):
        mailDeletar(email, itens)
    elif (esco == "5"):
        visualPedido(email, itens)
    elif (esco == "6"):
        clientes = {}
        clientes = finalizar(email, itens)
        print(clientes)
    elif (esco == "7"):
        #Para sair é verificado se o usario tem pedidos ou emails. O usuario decide se que sair
        if (len(email) == 0) or (len(itens) == 0):
            esco2 = input("Pedido não confirmado deseja sair SIM -> s NAO -> n: ")
            if (esco2 == "S") or (esco2 == "s"): 
                exit()
            else:
                main(email, itens)
    else:
        main(email, itens)

"""É necessário inicializar as listas, que está vazia aqui e chamar a função principal (main)
No caso para que não precise informar manualmente os dados é só editar as lista abaixo email
e itens como: 
            itens = [('desk', 3, 200,300,400), ('radio', 2, 400,550,1230)]
            onde os campos são[('nome', quantidade, unidade, peso, pacote)]
            email = ['azalu@yahoo.com', 'clamprayearth@gmail.com', 'isis@bol.com.br']
obs: Os valores monetarios aqui devem ser em centavos apenas, porém quando se inseri de forma 
manual o programa aceita em reais normalmente"""
itens = []
email = []
main(email, itens)