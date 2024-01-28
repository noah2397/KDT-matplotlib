import numpy
from matplotlib import pyplot as plot


X = numpy.linspace(-6, 6, 1024)
plot.plot(X, numpy.sinc(X), c = 'k') # 일반적인 그래프를 그려주고,

a = plot.axes([.6, .6, .25, .25]) # 그림 위에 부영역을 생성
# 그림 전체의 (0,0)은 하단 왼쪽 코너이며, (1,1)은 상단 오른쪽 코너이다
# axes로 왼쪽 코너의 좌표와 영역 크기로 부영역을 지정함!
# 또한, 부영역을 정의한 곳의 Axes 인스턴스를 a로 받음

X = numpy.linspace(-3, 3, 1024)
a.plot(X, numpy.sinc(X), c = 'k') # a.plot으로 그림을 그린 후
plot.setp(a) # setp를 호출하여 부영역 생성

plot.show()
