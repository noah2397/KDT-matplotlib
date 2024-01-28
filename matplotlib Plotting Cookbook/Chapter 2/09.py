import numpy
import matplotlib.cm as cm
import matplotlib.pyplot as plot

N = 256
angle  = numpy.linspace(0, 8 * 2 * numpy.pi, N) # 8바퀴를 도는 각도 생성
radius = numpy.linspace(.5, 1., N)

X = radius * numpy.cos(angle)
Y = radius * numpy.sin(angle)

#plot.scatter(X, Y, c = angle, cmap = cm.hsv)
# 컬러를 일일이 정의하지 않고, 컬러맵을 사용한다
# 컬러맵은 한 값의 연속적인 함수를 정의한다
# cm.hsv : 컬러의 전체 분광을  포함
# cm.PuOr : 과학 시각화, 인식 컬러 강도를 고려
plot.scatter(X, Y, c = angle, cmap = cm.PuOr)
plot.show()
