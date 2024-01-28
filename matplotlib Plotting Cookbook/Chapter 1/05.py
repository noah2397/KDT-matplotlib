import numpy
import matplotlib.pyplot as plot

#plt.show()는 지금까지 설명했던 그리고 싶은 곡선을 보여주라는 신호를 보낸다
def plot_slope(X, Y):
	Xs = X[1:] - X[:-1] # 99 개의 x변화량 생성
	Ys = Y[1:] - Y[:-1] # 99 개의 y변화량 생성
	plot.plot(X[1:], Ys / Xs) # 99개의 정의역으로, 기울기를 매번 표시

X = numpy.linspace(-3, 3, 100)
Y = numpy.exp(-X ** 2)

plot.plot(X, Y)
plot_slope(X, Y)
plot.show()
