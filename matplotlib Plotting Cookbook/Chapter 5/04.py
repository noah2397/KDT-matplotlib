import numpy
from matplotlib import pyplot as plot

X = numpy.linspace(-10, 10, 1024)
Y = numpy.sinc(X)

plot.plot(X, Y) # 72, 96, 150, 300
# 통상적인 800 X 600 화소 출력 대신에 2400 X 1800 화소가 된다
plot.savefig('sinc.png', dpi = 300)

# dpi : Dots Per inches(도트당 인치)
# 1 inch= 2.54 cm
# 기본적으로 dpi값이 100으로 설정되어있으므로,
# dpi=300 -> 800 X 600 -> 2400 X 1800 가 된다!
