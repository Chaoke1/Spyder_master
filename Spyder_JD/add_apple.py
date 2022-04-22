Apple="Apple"
op = open("data.txt", encoding='utf-8')
op_2 = open("Apple.csv", "w", encoding='utf-8')

lines = op.readlines()

for line in lines:
    if Apple in line:
        line = ",".join(line.split(" "))
        op_2.write(line)
 #   elif Samsung_2 in line:
  #      line = ",".join(line.split(" "))
   #     op_2.write(line)

op.close()
op_2.close()
