v_Entrada = int(input("Digite os segundos: "))
v_Horas = v_Entrada//(3600)
v_Aux = v_Entrada%3600
v_Minutos = v_Aux//60
v_Segundos = v_Minutos//60

print("Segundos =", v_Segundos)
print("Minutos =", v_Minutos)
print("Horas =", v_Horas)