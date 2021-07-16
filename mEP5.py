v_peso = float(input())
v_idade = int(input())
if (v_idade >= 16) and (v_idade <= 17):
    v_autori = input()
v_saude = input()
v_drogas = input()
v_pdoacao = input()
if (v_pdoacao == "n") or (v_pdoacao == "N"): 
    v_mesdoacao = int(input())
    v_ultidoacao = int(input())
v_sexo = input()
if (v_sexo == "f") or (v_sexo == "F"): 
    v_gravidez = input()
    v_amamentando = input()
    if (v_amamentando == "s") or (v_amamentando == "S"):  
        v_idadebebe = int(input())

v_boolpeso = v_peso >= 50
v_boolidade = (v_idade >= 16) and (v_idade <= 69)

if (v_idade >= 60) and (v_idade <= 69):
    if (v_pdoacao == "s") or (v_pdoacao == "S"):
        v_boolidade = False
    else:
        v_boolidade = True

if (v_saude == "s") or (v_saude == "S"):
    v_boolsaude = True
else:
    v_boolsaude = False

if (v_drogas == "n") or (v_drogas == "N"):
    v_booldrogas = True
else:
    v_booldrogas = False

if (v_pdoacao == "s") or (v_pdoacao == "S"):
    v_podedoar = True
else:
     v_podedoar = False    

if (v_sexo == "m") or (v_sexo == "M"):
    if (v_pdoacao == "n") or (v_pdoacao == "N"):
        if (v_mesdoacao <= 2) and (v_ultidoacao <= 4):
            v_podedoar = True 
        else:
            v_podedoar = False

if (v_sexo == "f") or (v_sexo == "F"):
    if (v_pdoacao == "n") or (v_pdoacao == "N"):
        if (v_mesdoacao <= 3) and (v_ultidoacao <= 3) and ((v_gravidez == "n") or (v_gravidez == "N")):
            v_podedoar = True 
        if (v_amamentando == "s") or (v_amamentando == "S"):
             if (v_idadebebe > 12):
                v_podedoar = True
        else:
            v_podedoar = False


print("Peso: {}".format(v_peso))
print("Idade: {}".format(v_idade))
if (v_idade >= 16) and (v_idade <= 17):
    print("Documento de autorizacao: {}".format(v_autori))
print("Boa saude: {}".format(v_saude))
print("Uso drogas injetaveis: {}".format(v_drogas))
print("Primeira doacao: {}".format(v_pdoacao))
if (v_pdoacao == "n") or (v_pdoacao == "N"):
    print("Meses desde ultima doacao: {}".format(v_mesdoacao))
    print("Doacoes nos ultimos 12 meses: {}".format(v_ultidoacao))
print("Sexo biologico: {}".format(v_sexo))
if (v_sexo == "f") or (v_sexo == "F"):
    print("Gravidez: {}".format(v_gravidez))
    print("Amamentando: {}".format(v_amamentando))
    if (v_amamentando == "s") or (v_amamentando == "S"):
        print("Meses bebe: {}".format(v_idadebebe))

if (v_podedoar == True) and (v_boolsaude  == True) and (v_boolpeso == True) and (v_boolidade == True) and (v_booldrogas == True):
    print("Procure um hemocentro.")
else:
    if (v_peso < 50):
        print("Impedimento: abaixo do peso minimo.")

    if (v_idade < 16):
        print("Impedimento: menor de 16 anos.")
    elif (v_idade < 18):
        if (v_autori == "n") or (v_autori == "N"):
            print("Impedimento: menor de 18 anos, sem consentimento dos responsaveis.")

    if (v_idade >= 60) and ((v_pdoacao == "s") or (v_pdoacao == "S")):
        print("Impedimento: maior de 60 anos , primeira doacao.")
    if (v_idade > 69):
        print("Impedimento: maior de 69 anos.")
    if (v_saude == "n") or (v_saude == "N"):
        print("Impedimento: nao esta em boa saude.")    
    if (v_drogas == "s") or (v_drogas == "S"):
        print("Impedimento: uso de drogas injetaveis.")
    if (v_pdoacao == "n") or (v_pdoacao == "N"):
        if (v_mesdoacao < 4) and ((v_sexo == "m") or (v_sexo == "M")):
            print("Impedimento: intervalo minimo entre as doacoes nao foi respeitado.")
    if (v_pdoacao == "n") or (v_pdoacao == "N"):
        if (v_mesdoacao < 3) and ((v_sexo == "f") or (v_sexo == "F")):
            print("Impedimento: intervalo minimo entre as doacoes nao foi respeitado.")
    if (v_pdoacao == "n") or (v_pdoacao == "N"):
        if (v_ultidoacao >= 4) and ((v_sexo == "m") or (v_sexo == "M")):
            print("Impedimento: numero maximo de doacoes anuais foi atingido.")
    if (v_pdoacao == "n") or (v_pdoacao == "N"):
        if (v_ultidoacao >= 3) and ((v_sexo == "f") or (v_sexo == "F")):
            print("Impedimento: numero maximo de doacoes anuais foi atingido.")
       
    if (v_sexo == "f") or (v_sexo == "F"):
        if (v_gravidez == "s") or (v_gravidez == "S"):
            print("Impedimento: gravidez.")
        if (v_amamentando == "s") or (v_amamentando == "S"):
            if (v_idadebebe < 12):
                print("Impedimento: amamentacao.")
