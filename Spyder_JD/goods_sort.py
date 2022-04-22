HUAWEI = "华为"
Redmi = "Redmi"
Apple = "Apple"
OPPO = "OPPO"
R_M = "realme"
Honer = "荣耀"
V_V = "vivo"
Samsung = "SAMSUNG"
Xiaomi = "小米"

op = open("data.txt", encoding='utf-8')
op_HUAWEI = open("HUAWEI.txt", "a", encoding='utf-8')
op_Redmi = open("Xiaomi.txt", "a", encoding='utf-8')
op_Apple = open("Apple.txt", "a", encoding='utf-8')
op_OPPO = open("OPPO.txt", "a", encoding='utf-8')
op_R_M = open("R_me.txt", "a", encoding='utf-8')
op_Honer = open("Honer.txt", "a", encoding='utf-8')
op_V_V = open("VV.txt", "a", encoding='utf-8')
op_Samsung = open("Sam.txt", "a", encoding='utf-8')
op_Xiaomi = open("Xiaomi.txt", "a", encoding='utf-8')

lines = op.readlines()
for line in lines:
    if HUAWEI in line:
        op_HUAWEI.write(line)

    if Apple in line:
        op_Apple.write(line)
    if OPPO in line:
        op_OPPO.write(line)
    if R_M in line:
        op_R_M.write(line)
    if Honer in line:
        op_Honer.write(line)
    if V_V in line:
        op_V_V.write(line)
    if Samsung in line:
        op_Samsung.write(line)
    if Xiaomi in line:
        op_Xiaomi.write(line)
    elif Redmi in line:
        op_Redmi.write(line)


op.close()
op_Apple.close()
op_Redmi.close()
op_HUAWEI.close()
op_OPPO.close()
op_R_M.close()
op_Xiaomi.close()
op_V_V.close()
op_Samsung.close()
op_Honer.close()