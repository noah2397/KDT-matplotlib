'''
import numpy
import matplotlib.pyplot as plot

X = numpy.linspace(0, 2 * numpy.pi, 100)
Y = numpy.sin(X)

plot.plot(X, Y)
plot.show()
'''

import math
import matplotlib.pyplot as plt

T=range(100)
print(len(T))
X=[(2*math.pi*t) / len(T) for t in T] # range타입의 len을 하면 그만큼의 길이가 나온다, 총 100개의 정의역 생성
print(X)
Y=[math.sin(value) for value in X] # 삼각함수의 값 생성
plt.plot(X,Y)
plt.show()