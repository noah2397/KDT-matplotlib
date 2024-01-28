import numpy
import matplotlib.pyplot as plot

X = numpy.linspace(-6, 6, 1024)

plot.ylim(-.5, 1.5) # ylim을 사용하여 y축의 범위값을 설정한다
plot.plot(X, numpy.sinc(X), c = 'k')

plot.show()
