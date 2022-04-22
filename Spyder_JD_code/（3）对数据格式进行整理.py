jd_1 = "京东国际"
jd_2 = "京品手机"

op = open("goods_List.txt", encoding='utf-8')
op_2 = open("data.txt", "a", encoding='utf-8')
lines = op.readlines()

for line in lines:
    if jd_1 in line:
        line = line.strip('\n')
    if jd_2 in line:
        line = line.strip('\n')
    op_2.write(line)
op.close()
op_2.close()
