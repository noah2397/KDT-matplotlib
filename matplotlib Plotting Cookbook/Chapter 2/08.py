import random
import matplotlib.pyplot as plot

values = [random.gauss(0., 1.) for i in range(100)]

b = plot.boxplot(values)
for name, line_list in b.items():
	for line in line_list:
		print(line)
		line.set_color('k')

plot.show()
