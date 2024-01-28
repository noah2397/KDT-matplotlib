import numpy
import matplotlib.pyplot as plot

X = numpy.linspace(-100, 100, 4096)

# symlog를 사용한 xscale 조정
# linethresh=6을 설정함으로써 [-6,6]범위 지정
plot.xscale('symlog', linthresh=6.)

plot.plot(X, numpy.sinc(X), c = 'k')
plot.show()
