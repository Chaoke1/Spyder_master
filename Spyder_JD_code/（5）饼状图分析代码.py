import csv

from matplotlib import pyplot as plt
import pandas as pd
import numpy as np

fig = plt.figure("华为价格分析")
ax = fig.add_axes([0, 0, 1, 1])
# 使得X/Y轴的间距相等

Low_price = Num_nom = Num_mid = Num_high = 0
with open("X_R_mi.csv", "r") as csvfile:
    reader = csv.reader(csvfile)
    for line in reader:
        if float(line[0]) <= 2200:
            Low_price += 1
        elif float(line[0]) <= 3500:
            Num_nom += 1
        elif float(line[0]) <= 6000:
            Num_mid += 1
        elif float(line[0]) > 6000:
            Num_high += 1

ax.axis('equal')
langs = ['Low_Price part', 'Normal_Price part', 'Mid_Price part', 'High_Price part']
Part_name = [Low_price, Num_nom, Num_mid, Num_high]
colors = ['springgreen', 'darkorchid', 'royalblue', 'deeppink']
# 绘制饼状图
ax.pie(Part_name, labels=langs, colors=colors, autopct='%1.2f%%', shadow='true')
plt.show()
