salario = float(input())
imposto = 0

if (salario > 4500):
    aux = salario - 4500
    indice = aux * 0.28
    imposto += indice
    indice = 1500 * 0.18
    imposto += indice
    indice = 1000 * 0.08
    imposto += indice
    print("R$ {:.2f}".format(imposto))
elif (salario <= 4500) and (salario > 3000):
    aux = salario - 3000
    indice = aux * 0.18
    imposto += indice
    indice = 1000 * 0.08
    imposto += indice
    print("R$ {:.2f}".format(imposto))
elif (salario <= 3000) and (salario > 2000):
    aux = salario - 2000
    indice = aux * 0.08
    imposto += indice
    print("R$ {:.2f}".format(imposto))
else:    
    print("Isento")
