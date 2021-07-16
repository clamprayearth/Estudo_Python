def RadToDegre(rad):
    """Converte um ângulo dado de radiano para grau.
       Args: deg ângulo em radiano;
       returns: ângulo em grau.
    """
    return((rad*180.0)/3.14)

rad=float(input('Entre com o ângulo em radiano: '))
deg=RadToDegre(rad)
print(rad,' radinaos = ' ,deg,'º')