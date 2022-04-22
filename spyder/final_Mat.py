import matplotlib.pyplot as plt

fig = plt.figure()

ax = fig.add_axes([0.1, 0.1, 0.9, 0.9])

Name_brand = ['Apple', 'HUAWEI', 'Honor', 'Samsung', 'OPPO', 'ViVo', 'Xiao&Red mi']
percent = [52.05, 16, 2.70, 37.50, 2.62, 1.58, 2.44]

colors = ['hotpink', 'deepskyblue', 'lightcoral', 'plum', 'cyan', 'navajowhite', 'springgreen']
ax.bar(Name_brand, percent, color=colors)
plt.show()
