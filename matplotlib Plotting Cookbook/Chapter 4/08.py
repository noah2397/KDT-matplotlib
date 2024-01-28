import numpy
import matplotlib.pyplot as plot

T = numpy.linspace(0 , 2 * numpy.pi, 1024)

# 극좌표(Polar coordinate)를 자연스럽게 선택
# 년별, 일별 통계 같은 주기적인 데이터를 극 좌표계로 편리하게 그릴 수 있다

plot.axes(polar = True)
plot.plot(T, 1. + .25 * numpy.sin(16 * T), c = 'k') # 주기가 pi/8인 사인함수 그리기

plot.show()
