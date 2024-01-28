import numpy
from matplotlib import pyplot as plot

X = numpy.linspace(-6, 6, 1024)
plot.plot(X, numpy.sinc(X))
plot.xticks([]) # 빈 리스트를 주어 x라벨, y라벨 없앰
plot.yticks([])
plot.show()
