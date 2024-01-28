import numpy as np
import matplotlib.pyplot as plt
'''
data = numpy.array([[5., 30., 45., 22.],
                    [5., 25., 50., 20.],
                    [1.,  2.,  1.,  1.]])

color_list = ['b', 'g', 'r']
X = range(data.shape[1])
for i, col in enumerate(color_list):
	plot.bar(X, data[i], bottom = numpy.sum(data[:i], axis = 0), color = col)

plot.show()
'''

A=np.array([5,30,45,22])
B=np.array([5,25,50,20])
C=np.array([1,2,1,1])
X=np.arange(4)

plt.bar(X,A)
plt.bar(X,B,bottom=A)
plt.bar(X,C,bottom=A+B)
plt.show()
