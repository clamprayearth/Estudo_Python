def classe(a, countPar, countImpar, countPosi, countNega):
    if a % 2 == 0:
        countPar+=1
    else:
        countImpar+=1
    if a > 0:
        countPosi+=1
    elif a < 0:
        countNega+=1
    return countPar, countImpar, countPosi, countNega

num1 = int(input())
num2 = int(input())
num3 = int(input())
num4 = int(input())
num5 = int(input())
contPar = 0
contImpar = 0
contPosi = 0
contNega = 0
contPar, contImpar, contPosi, contNega = classe(num1, contPar, contImpar, contPosi, contNega)
contPar, contImpar, contPosi, contNega = classe(num2, contPar, contImpar, contPosi, contNega)
contPar, contImpar, contPosi, contNega = classe(num3, contPar, contImpar, contPosi, contNega)
contPar, contImpar, contPosi, contNega = classe(num4, contPar, contImpar, contPosi, contNega)
contPar, contImpar, contPosi, contNega = classe(num5, contPar, contImpar, contPosi, contNega)

print("{} valor(es) par(es)".format(contPar))
print("{} valor(es) impar(es)".format(contImpar))
print("{} valor(es) positivo(s)".format(contPosi))
print("{} valor(es) negativo(s)".format(contNega))