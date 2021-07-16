v_Hs = 7
v_Ms = 20
v_Hc = 8
v_Mc = 15
v_mToSaida = v_Hs * 60 + v_Ms
v_mToChegada = v_Hc * 60 + v_Mc
v_Total = v_mToChegada - v_mToSaida
v_Horas = v_Total // 60
v_Minutos = v_Total%60
print(v_Horas)
print(v_Minutos)
