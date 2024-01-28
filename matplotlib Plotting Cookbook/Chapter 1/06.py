import matplotlib.pyplot as plot

X, Y, Z = zip(*[[float(s) for s in line.split()] for line in open(r'sample.txt', 'r')])

plot.plot(X, Y)
plot.show()
