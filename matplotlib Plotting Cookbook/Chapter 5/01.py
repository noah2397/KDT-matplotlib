import numpy
from matplotlib import pyplot as plot

X = numpy.linspace(-10, 10, 1024)
Y = numpy.sinc(X)

plot.plot(X, Y, c = 'k')
# savefig를 사용하여 현재 경로에 png파일을 생성함
plot.savefig('sinc.png')
