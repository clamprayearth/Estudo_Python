n_Lado1 = int(input())
n_Lado2 = int(input())
n_Lado3 = int(input())

if (n_Lado1 <= 0) or (n_Lado2 <= 0) or (n_Lado3 <= 0):

    print("Valores invalidos.")

elif (n_Lado1 >= n_Lado2 + n_Lado3) or (n_Lado2 >= n_Lado1 + n_Lado3) or (n_Lado3 >= n_Lado1 + n_Lado2):

    print("Valores nao podem formar um triangulo.")

else:

    if (n_Lado1 == n_Lado2) and (n_Lado3 == n_Lado2) and (n_Lado1 == n_Lado3):
        print("Triangulo equilatero.")
    elif (n_Lado1 == n_Lado2) or (n_Lado3 == n_Lado2) or (n_Lado1 == n_Lado3):
        print("Triangulo isosceles.")
    elif (n_Lado1 != n_Lado2) and (n_Lado3 != n_Lado2) and (n_Lado1 != n_Lado3):
        print("Triangulo escaleno.")

    if (n_Lado1 > n_Lado2) and (n_Lado1 > n_Lado3):

        if (n_Lado1**2 == n_Lado2**2 + n_Lado3**2):
            print("Triangulo retangulo.")
        elif (n_Lado1**2 < n_Lado2**2 + n_Lado3**2):
            print("Triangulo acutangulo.")
        elif (n_Lado1**2 > n_Lado2**2 + n_Lado3**2):
            print("Triangulo obtusangulo.")

    elif (n_Lado2 > n_Lado1) and (n_Lado2 > n_Lado3):

        if (n_Lado2**2 == n_Lado1**2 + n_Lado3**2):
            print("Triangulo retangulo.")
        elif (n_Lado2**2 < n_Lado1**2 + n_Lado3**2):
            print("Triangulo acutangulo.")
        elif (n_Lado2**2 > n_Lado1**2 + n_Lado3**2):
            print("Triangulo obtusangulo.")

    elif (n_Lado3 > n_Lado1) and (n_Lado3 > n_Lado2):

        if (n_Lado3**2 == n_Lado1**2 + n_Lado2**2):
            print("Triangulo retangulo.")
        elif (n_Lado3**2 < n_Lado1**2 + n_Lado2**2):
            print("Triangulo acutangulo.")
        elif (n_Lado3**2 > n_Lado1**2 + n_Lado2**2):
            print("Triangulo obtusangulo.")

    else:
        print("Triangulo acutangulo.")

