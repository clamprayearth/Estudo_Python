def trataentrada(tempo, idade, sexo):
    if (tempo <= 0):
        return False
    elif (idade < 18):
        return False
    elif (sexo !="M") and (sexo !="m") and (sexo !="F") and (sexo !="f"):
        return False
    else:
        return True
def indice(idade, sexo):
    if (sexo == "M") or (sexo == "m"):
        if (idade >= 18) and (idade <= 34):
            return 3 * 60
        elif (idade >= 35) and (idade <= 39):
            return 3 * 60 + 5
        elif (idade >= 40) and (idade <= 44):
            return 3 * 60 + 10
        elif (idade >= 45) and (idade <= 49):
            return 3 * 60 + 20
        elif (idade >= 50) and (idade <= 54):
            return 3 * 60 + 25
        elif (idade >= 55) and (idade <= 59):
            return 3 * 60 + 35
        elif (idade >= 60) and (idade <= 64):
            return 3 * 60 + 50
        elif (idade >= 65) and (idade <= 69):
            return 4 * 60 + 5
        elif (idade >= 70) and (idade <= 74):
            return 4 * 60 + 20
        elif (idade >= 75) and (idade <= 79):
            return 4 * 60 + 35
        else:
            return 4 * 60 + 50
    elif (sexo == "F") or (sexo == "f"):
        if (idade >= 18) and (idade <= 34):
            return 3 * 60 + 30
        elif (idade >= 35) and (idade <= 39):
            return 3 * 60 + 35
        elif (idade >= 40) and (idade <= 44):
            return 3 * 60 + 40
        elif (idade >= 45) and (idade <= 49):
            return 3 * 60 + 50
        elif (idade >= 50) and (idade <= 54):
            return 3 * 60 + 55
        elif (idade >= 55) and (idade <= 59):
            return 4 * 60 + 5
        elif (idade >= 60) and (idade <= 64):
            return 4 * 60 + 20
        elif (idade >= 65) and (idade <= 69):
            return 4 * 60 + 35
        elif (idade >= 70) and (idade <= 74):
            return 4 * 60 + 50
        elif (idade >= 75) and (idade <= 79):
            return 5 * 60 + 5
        else:
            return 5 * 60 + 20
def saida(tempo, tempomax, boston, sexo):
    if (sexo == "M") or (sexo == "m"):
        print("Tempo do corredor: {0:02d}h {1:02d}min".format(tempo//60, tempo%60))
        print("Tempo necessario: {0:02d}h {1:02d}min".format(tempomax//60, tempomax%60))
        if boston:
            print("Conseguiu indice? SIM")
            print("O corredor correu {0:02d}h {1:02d}min abaixo do indice".format((tempomax - tempo)//60, (tempomax - tempo)%60))
        else:
            print("Conseguiu indice? NAO")
            print("O corredor correu {0:02d}h {1:02d}min acima do indice".format((tempo - tempomax)//60, (tempo - tempomax)%60))
    elif (sexo == "F") or (sexo == "f"):
        print("Tempo da corredora: {0:02d}h {1:02d}min".format(tempo//60, tempo%60))
        print("Tempo necessario: {0:02d}h {1:02d}min".format(tempomax//60, tempomax%60))
        if boston:
            print("Conseguiu indice? SIM")
            print("A corredora correu {0:02d}h {1:02d}min abaixo do indice".format((tempomax - tempo)//60, (tempomax - tempo)%60))
        else:
            print("Conseguiu indice? NAO")
            print("A corredora correu {0:02d}h {1:02d}min acima do indice".format((tempo - tempomax)//60, (tempo - tempomax)%60))
        
def main():
    v_Tempo = int(input())
    v_Idade = int(input())
    v_Sexo = input()

    if trataentrada(v_Tempo, v_Idade, v_Sexo):
        v_TempoMax = indice(v_Idade, v_Sexo)
        if (v_Tempo <= v_TempoMax):
            saida(v_Tempo, v_TempoMax, True, v_Sexo)
        else:
            saida(v_Tempo, v_TempoMax, False, v_Sexo)

main()

