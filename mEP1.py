v_Num1 = float(input())
v_Operacao = input()
v_Num2 = float(input())

if (v_Operacao != "+") and (v_Operacao != "-") and (v_Operacao != "*") and (v_Operacao != "/") and (v_Operacao != "//") and (v_Operacao != "**") and (v_Operacao != "%"):
    print("“OPERACAO NAO RECONHECIDA”")    
else:
    if v_Operacao == "+":
        v_Result = v_Num1 + v_Num2
        print("{} + {} = {}".format(v_Num1, v_Num2, v_Result))
    if v_Operacao == "-":
        v_Result = v_Num1 - v_Num2
        print("{} - {} = {}".format(v_Num1, v_Num2, v_Result))
    if v_Operacao == "*":
        v_Result = v_Num1 * v_Num2
        print("{} * {} = {}".format(v_Num1, v_Num2, v_Result))
    if v_Operacao == "/":
        v_Result = v_Num1 / v_Num2
        print("{} / {} = {}".format(v_Num1, v_Num2, v_Result))
    if v_Operacao == "//":
        v_Result = v_Num1 // v_Num2
        print("{} // {} = {}".format(v_Num1, v_Num2, v_Result))
    if v_Operacao == "**":
        v_Result = v_Num1 ** v_Num2
        print("{} ** {} = {}".format(v_Num1, v_Num2, v_Result))
    if v_Operacao == "%":
        v_Result = v_Num1 % v_Num2
        print("{} % {} = {}".format(v_Num1, v_Num2, v_Result))
