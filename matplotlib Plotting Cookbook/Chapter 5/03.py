import numpy
from matplotlib import pyplot as plot

X = numpy.linspace(-10, 10, 1024)
Y = numpy.sinc(X)

plot.plot(X, Y)
# 그림의 내용에 맞게 자동으로 여백을 조절
plot.savefig('sinc.png', bbox_inches = 'tight')
