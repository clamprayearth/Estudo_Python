nome = input()
salario = float(input())
vendas = float(input())

if (salario > 0) and (vendas >= 0):
    total = salario + vendas * 0.15

print("TOTAL = R$ {:.2F}".format(total))