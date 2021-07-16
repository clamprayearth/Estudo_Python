def mediaP(p):
    return (2*p[0] + 3*p[1]) / 5

def mediaEP(Ep):
    return (Ep[0] + Ep[1]) / 2

def mediamEp(qt, mEp, pesomEp):
    if (qt > 0):
        nota = float(input())
        peso = int(input())
        mEp = mEp + [nota]
        pesomEp = pesomEp + [peso]
        return mediamEp(qt -1, mEp, pesomEp)
    else:
        return mediaauxPo(mEp, pesomEp, len(mEp))

def mediaLista(qt, mLista):
    if (qt > 0):
        nota = float(input())
        mLista = mLista + [nota]
        return mediaLista(qt -1, mLista)
    else:
        return mediaaux(mLista, len(mLista))

def mediaPratica(qt, Pratica):
    if (qt > 0):
        nota = float(input())
        Pratica = Pratica + [nota]
        return mediaPratica(qt-1, Pratica)
    else:
        return mediaaux(Pratica, len(Pratica))
    
def mediaaux(nota, count, soma = 0):
    if (count > 0):
        soma = soma + nota[count-1]
        return mediaaux(nota, count - 1, soma)
    else:
        media = soma / len(nota)
        return media

def mediaauxPo(nota, peso, count, soma = 0, somapeso = 0):
    if (count > 0):
        soma = soma + nota[count-1] * peso[count-1]
        somapeso = somapeso + peso[count-1]
        return mediaauxPo(nota, peso, count - 1, soma, somapeso)
    else:
        media = soma / somapeso
        return media
    
def main():
    p = [0,0]
    Ep = [0,0]
    mEp = []
    pesomEp = []
    Lista = []
    Pratica = []
    frequencia = float(input())
    p[0] = float(input())
    p[1] = float(input())
    pmedia = mediaP(p)
    Ep[0] = float(input())
    Ep[1] = float(input())
    Epmedia = mediaEP(Ep)
    qt = int(input())
    mEpmedia = mediamEp(qt, mEp, pesomEp)
    qt = int(input())
    Listamedia = mediaLista(qt, Lista)
    qt = int(input())
    Praticamedia = mediaPratica(qt, Pratica)
    mediaParcial = 0.55 * pmedia + 0.25 * Epmedia + 0.15 * mEpmedia + 0.10 * Listamedia + 0.05 * Praticamedia

    print("Media (ponderada) das provas: {0:.1f}".format(pmedia))
    print("Media dos EPs: {0:.1f}".format(Epmedia))
    print("Media (ponderada) dos miniEPs: {0:.1f}".format(mEpmedia))
    print("Media das listas de exercicios: {0:.1f}".format(Listamedia))
    print("Media das aulas praticas: {0:.1f}".format(Praticamedia))
    print("Frequencia: {0:.1f}%".format(frequencia))
    print("Media parcial: {0:.1f}".format(mediaParcial))
   
   
    if (mediaParcial >= 7):
        mediaFinal = mediaParcial
        print("Media final: {0:.1f}".format(mediaFinal))
    else:
        x = float(input())
        mediaFinal = (mediaParcial + x) / 2
        print("Prova final: {0:.1f}".format(x))
        print("Media final: {0:.1f}".format(mediaFinal))
        
    if (frequencia >= 75):
        if (mediaFinal >= 5):
            print("Aprovado(a) por nota e frequencia.")
        else:
            print("Reprovado(a) por nota.")
    else:
        print("Reprovado(a) por frequencia.")
main()