import numpy
from matplotlib import pyplot as plot

X = numpy.linspace(-10, 10, 1024)
Y = numpy.sinc(X)

plot.plot(X, Y, c = 'k')
# transparent를 True로 주어 투명한 이미지 PNG형태로 출력
plot.savefig('sinc.png', transparent = True)
